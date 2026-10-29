"""Typed image coordinates. Never relocate arbitrary integers or heap pointers."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ImageCoordinates:
    input_md5: str
    capture_base: int
    idb_base: int
    runtime_base: int = None

    def __post_init__(self):
        if not self.input_md5 or min(self.capture_base, self.idb_base) < 0:
            raise ValueError("Invalid image identity or base")
        if self.runtime_base is not None and self.runtime_base < 0:
            raise ValueError("Invalid runtime base")

    def rva(self, capture_ea):
        result = capture_ea - self.capture_base
        if result < 0:
            raise ValueError("Address precedes captured image base")
        return result

    def current_ea(self, rva):
        if rva < 0:
            raise ValueError("Negative RVA")
        return self.idb_base + rva

    def runtime_va(self, rva):
        if self.runtime_base is None:
            raise ValueError("Runtime mapping not established")
        if rva < 0:
            raise ValueError("Negative RVA")
        return self.runtime_base + rva

    def reference(self, capture_ea):
        rva = self.rva(capture_ea)
        return {"space": "image", "capture_ea": capture_ea, "capture_base": self.capture_base,
                "rva": rva, "current_ea": self.current_ea(rva),
                "runtime_va": self.runtime_va(rva) if self.runtime_base is not None else None}

    def assert_current(self, identity):
        if identity.get("input_md5") != self.input_md5 or identity.get("imagebase") != self.idb_base:
            raise ValueError("Image identity/base changed; discard mapping validation and establish it again")
