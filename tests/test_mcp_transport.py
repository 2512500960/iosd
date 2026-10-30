import json
import unittest
from unittest.mock import Mock,patch

from tools.ida_mcp_client import McpClient
from test_skill_mcp import cli


class CompletedOutputTests(unittest.TestCase):
    def test_large_python_result_downloaded_once_without_another_tool_execution(self):
        metadata={'_output_truncated':True,'_download_url':'http://fixture:13337/output/ab-123.json','_output_id':'ab-123'}
        client=Mock();client.send.return_value={'structuredContent':metadata}
        client.download_output.return_value={'stdout':'complete evidence','stderr':''}
        self.assertEqual(cli.tool_result(client,'read_only()'),'complete evidence')
        client.send.assert_called_once();client.download_output.assert_called_once_with(metadata['_download_url'],'ab-123')

    def test_cross_origin_and_non_output_paths_are_rejected_before_http(self):
        client=McpClient('http://fixture:13337/mcp')
        with patch('urllib.request.build_opener') as opener:
            for url in ('http://other:13337/output/ab-123.json','http://fixture:13338/output/ab-123.json',
                        'http://fixture:13337/mcp','http://fixture:13337/output/ab-123.json?x=1'):
                with self.assertRaises(ValueError):client.download_output(url,'ab-123')
            opener.assert_not_called()

    def test_download_preserves_complete_json_and_refuses_another_preview(self):
        client=McpClient('http://fixture:13337/mcp');response=Mock()
        response.__enter__=Mock(return_value=response);response.__exit__=Mock(return_value=False)
        with patch('urllib.request.build_opener') as builder:
            builder.return_value.open.return_value=response
            response.read.return_value=json.dumps({'stdout':'x'*75000,'stderr':''}).encode()
            result=client.download_output('http://fixture:13337/output/ab-123.json','ab-123')
            self.assertEqual(len(result['stdout']),75000)
            response.read.return_value=b'{"_output_truncated":true}'
            with self.assertRaisesRegex(ValueError,'complete'):client.download_output('http://fixture:13337/output/ab-123.json','ab-123')


if __name__=='__main__':unittest.main()
