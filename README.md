# PipeRun Extractor

Biblioteca Python 3.11+ para extração de dados dos endpoints do CRM PipeRun de Vendas

## Instalação
Instalação global ou por projeto utilizando a ferramenta `pip` 21+
```shell
python3 -m pip install git+https://github.com/crmpiperun/piperun-extractor
```
Instalação por usuário usando [pipx](https://github.com/pypa/pipx)
```shell
pipx install git+https://github.com/crmpiperun/piperun-extractor
```

## Uso como CLI
```shell
piperun-extractor --help
piperun-extractor deals --token "abcdefghijklmnopqrstuvwxyz" --after "2025-01-01T00:00:00" --ext jsonl --output deals.jsonl
```

```
Usage: piperun-extractor [OPTIONS] METHOD
Options:
  -t, --token TEXT                          User Token            [required]
  -a, --after [%Y-%m-%dT%H:%M:%S]           Date to start filter  [required]
  -e, --ext [jsonl|parquet]                 Output Extension      [required, default: jsonl]
  -o, --output TEXT                         Output Location       [required]
  --log [critical|error|warning|info|debug] Log level             [default: warning]
```
O argumento `METHOD` pode ser qualquer um dos métodos disponíves na listagem abaixo.
Ou pode ser `all` para extrair todos os dados, porém para este argumento a opção `--output` DEVE ser um diretório,
onde serão gravados os arquivos com o nome de cada método e com o formato definido em `--ext`
> [!TIP]
> Se você está fazendo uma carga incremental usando `all` todos os arquivos serão sobrescritos, este comando não faz mesclagem das informações.

## Uso como Biblioteca
```python
from datetime import datetime
from piperun.extractor import PipeRunExtractor

extractor = PipeRunExtractor(token='abcdefghijklmnopqrstuvwxyz')
deals = extractor.deals(after=datetime(2025, 1, 1))

for deal in deals:
    print(deal.title)
```

O objeto `PipeRunExtractor` possui métodos para todas as entidades mapeadas para extração.
Esses métodos recebem como argumento um `datetime` denominado `after` obrigatório,
caso seja necessário recuperar toda a informação contida no sistema, use uma data que anteceda a criação da sua conta,
isso garantirá que todos os dados sejam recuperados.
Prefira usar essa tática somente para a primeira carga, escolhendo uma data adequada para as requisições posteriores, 
garantindo assim uma carga incremental muito mais rápida.

## Métodos Disponíveis
```
users                           Iterator[schema.users.User]
users_teams                     Iterator[schema.users.Team]
users_team_groups               Iterator[schema.users.TeamGroup]
pipelines                       Iterator[schema.pipeline.Pipeline]
pipelines_stages                Iterator[schema.pipeline.Stage]
deals                           Iterator[schema.deals.Deal]
deals_stage_histories           Iterator[schema.deals.StageHistory]
deals_lost_reasons              Iterator[schema.deals.LostReason]
companies                       Iterator[schema.companies.Company]
companies_segments              Iterator[schema.companies.Segment]
persons                         Iterator[schema.person.Person]
activities                      Iterator[schema.activities.Activity]
activities_types                Iterator[schema.activities.ActivityType]
proposals                       Iterator[schema.proposals.Proposal]
proposal_model                  Iterator[schema.proposals.ProposalModel]
proposal_layout                 Iterator[schema.proposals.ProposalLayout]
proposals_payment_methods       Iterator[schema.proposals.PaymentMethod]
proposals_payment_methods_types Iterator[schema.proposals.PaymentMethodsType]
proposals_parcel                Iterator[schema.proposals.ProposalParcel]
proposals_parcel_payments       Iterator[schema.proposals.proposalParcelPayments]
cities                          Iterator[schema.cities.City]
calls                           Iterator[schema.calls.Call]
custom_fields                   Iterator[schema.custom_fields.CustomFieldResponse]
deals_has_custom_fields         Iterator[schema.custom_fields.EntityHasCustomField]
companies_has_custom_fields     Iterator[schema.custom_fields.EntityHasCustomField]
persons_has_custom_fields       Iterator[schema.custom_fields.EntityHasCustomField]
custom_forms                    Iterator[schema.custom_forms.CustomForm]
notes                           Iterator[schema.notes.Note]
items                           Iterator[schema.items.Item]
items_characteristics           Iterator[schema.items.Characteristic]
items_categories                Iterator[schema.items.Category]
items_measurement_units         Iterator[schema.items.MeasurementUnit]
datalists                       Iterator[schema.data_lists.DataList]
tags                            Iterator[schema.tags.Tag]
cnaes                           Iterator[schema.cnaes.Cnae]
emails                          Iterator[schema.emails.Email]
emails_templates                Iterator[schema.emails.EmailTemplate]
origins                         Iterator[schema.origins.Origin]
origins_groups                  Iterator[schema.origins.OriginGroup]
regions                         Iterator[schema.regions.Region]
```
