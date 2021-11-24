# Disponibilidade NFe

[![Test](https://github.com/leogregianin/disponibilidade-nfe/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/leogregianin/disponibilidade-nfe/actions/workflows/main.yml)

Projeto de Web scraping para verificar a disponibilidade dos Webservices de todas as Secretarias de Fazenda (Sefaz) emitente de Nota Fiscal Eletrônica (NFe) através do Portal Nacional da NFe: http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx


## Instalar

```console
$ poetry install
```

## Rodar testes

```console
$ poetry run tox
```

## Exemplos

```python
from disponibilidade_nfe.nfe import DisponibilidadeNFe

disp_nfe = DisponibilidadeNFe()
print(disp_nfe.get_status())
```

Resultado:
```console
[
    {
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
    }, {
        'autorizador': 'BA',
        'autorizacao': 'verde',
        'retorno_autorizacao': 'verde',
        'inutilizacao': 'verde',
        'consulta_protocolo': 'verde',
        'status_servico': 'verde',
        'tempo_medio': '-',
        'consulta_cadastro': 'verde',
        'recepcao_evento': 'verde',
        'ultima_verificacao': '23/11/2021 23:06:31'
    }, {
        ...
    }
]
```

## License

This package is licensed under [MIT license](/LICENSE).