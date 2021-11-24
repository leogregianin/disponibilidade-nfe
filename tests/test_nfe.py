import requests
import unittest
import requests_mock
import json

from disponibilidade_nfe.nfe import DisponibilidadeNFe


class GetDisponilidadeNFeTestCase(unittest.TestCase):

    def setUp(self):
        self.disp_nfe = DisponibilidadeNFe()

    @requests_mock.Mocker()
    def test_primeiro_autorizador(self, request_mock):
        url = 'https://foo.bar'
        data = {
            'autorizador': 'AM',
            'autorizacao': 'verde',
            'retorno_autorizacao': 'verde',
            'inutilizacao': 'verde',
            'consulta_protocolo': 'verde',
            'status_servico': 'verde',
            'tempo_medio': '-',
            'consulta_cadastro': '',
            'recepcao_evento': 'verde',
            'ultima_verificacao': '23/11/2021 23:06:31'
        }
        request_mock.get(url, json=data)
        # resp = self.disp_nfe.get_status()
        r = requests.get(url).text
        resp = json.loads(r)

        self.assertEqual(resp, data)
        self.assertEqual(resp.get('autorizador'), 'AM')
        self.assertEqual(resp.get('autorizacao'), 'verde')
        self.assertEqual(resp.get('retorno_autorizacao'), 'verde')
        self.assertEqual(resp.get('inutilizacao'), 'verde')
        self.assertEqual(resp.get('consulta_protocolo'), 'verde')
        self.assertEqual(resp.get('status_servico'), 'verde')
        self.assertEqual(resp.get('tempo_medio'), '-')
        self.assertEqual(resp.get('consulta_cadastro'), '')
        self.assertEqual(resp.get('recepcao_evento'), 'verde')
        self.assertEqual(resp.get('ultima_verificacao'), '23/11/2021 23:06:31')


if __name__ == '__main__':
    unittest.main()
