import pytest


@pytest.fixture
def list_of_dict_fixt_initial():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_fixt_executed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_of_dict_fixt_cancel():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_fixt_no_state():
    return [
        {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_fixt_wrong_state():
    return [
        {"id": 41428829, "state": 12345, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": (), "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": 89.02, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_fixt_date_sort_desc():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_of_dict_fixt_date_sort_asc():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_of_dict_fixt_equaldates_initial():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_of_dict_fixt_equaldates_sort_desc():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_of_dict_fixt_equaldates_sort_asc():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_of_dict_fixt_wrong_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "20190703T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "264"},
        {"id": 615064591, "state": "CANCELED", "date": "20118:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T1829.512364"},
    ]


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_USD_1():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def transactions_USD_2():
    return {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


@pytest.fixture
def transactions_USD_3():
    return {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


@pytest.fixture
def transactions_eur_1():
    return {
        "id": 939719574,
        "state": "EXECUTED",
        "date": "2018-05-30T02:08:58.425572",
        "operationAmount": {"amount": "9724.07", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def transactions_RUB_1():
    return {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


@pytest.fixture
def transactions_no_curr():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": ""}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "", "code": ""}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "", "code": ""}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "", "code": ""}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def descriptions():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def json_list_initial():
    return [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        },
        {
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "id": 41428829,
            "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 35383033474447895560",
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "id": 587085106,
            "operationAmount": {"amount": "48223.05", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 41421565395219882431",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-12-20T16:43:26.929246",
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "id": 214024827,
            "operationAmount": {"amount": "70946.18", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 21969751544412966366",
        },
        {
            "date": "2019-07-12T20:41:47.882230",
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "id": 522357576,
            "operationAmount": {"amount": "51463.70", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 38976430693692818358",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "date": "2018-07-11T02:26:18.671407",
            "description": "Открытие вклада",
            "id": 596171168,
            "operationAmount": {"amount": "79931.03", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 72082042523231456215",
        },
        {
            "date": "2018-04-04T17:33:34.701093",
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "id": 716496732,
            "operationAmount": {"amount": "40701.91", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 72731966109147704472",
        },
        {
            "date": "2019-12-08T22:46:21.935582",
            "description": "Открытие вклада",
            "id": 863064926,
            "operationAmount": {"amount": "41096.24", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 90424923579946435907",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
        {
            "date": "2018-10-14T08:21:33.419441",
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "id": 615064591,
            "operationAmount": {"amount": "77751.04", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 84163357546688983493",
        },
        {
            "date": "2018-01-26T15:40:13.413061",
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "id": 147815167,
            "operationAmount": {"amount": "50870.71", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 43597928997568165086",
        },
        {
            "date": "2018-11-29T07:18:23.941293",
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "id": 518707726,
            "operationAmount": {"amount": "3348.98", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Gold 9447344650495960",
        },
        {
            "date": "2018-04-14T19:35:28.978265",
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "id": 649467725,
            "operationAmount": {"amount": "96995.73", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 97584898735659638967",
        },
        {
            "date": "2019-09-11T17:30:34.445824",
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "id": 782295999,
            "operationAmount": {"amount": "54280.01", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 96291777776753236930",
        },
        {
            "date": "2018-10-14T22:27:25.205631",
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "id": 542678139,
            "operationAmount": {"amount": "90582.51", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 78808375133947439319",
        },
        {
            "date": "2019-04-12T17:27:27.896421",
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "id": 558167602,
            "operationAmount": {"amount": "43861.89", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 89685546118890842412",
        },
        {
            "date": "2018-02-03T14:52:08.093722",
            "description": "Перевод с карты на карту",
            "from": "MasterCard 4047671689373225",
            "id": 407169720,
            "operationAmount": {"amount": "67011.26", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Maestro 3806652527413662",
        },
        {
            "date": "2018-03-02T02:03:11.563721",
            "description": "Перевод организации",
            "from": "Счет 96008924215040031147",
            "id": 361044570,
            "operationAmount": {"amount": "7484.91", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 30377212495530283001",
        },
        {
            "date": "2018-06-12T07:17:01.311610",
            "description": "Перевод организации",
            "from": "Visa Classic 4195191172583802",
            "id": 536723678,
            "operationAmount": {"amount": "26334.08", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 17066032701791012883",
        },
        {
            "date": "2018-12-28T23:10:35.459698",
            "description": "Открытие вклада",
            "id": 172864002,
            "operationAmount": {"amount": "49192.52", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 96231448929365202391",
        },
        {
            "date": "2018-11-23T17:47:33.127140",
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 7305799447374042",
            "id": 476991061,
            "operationAmount": {"amount": "26971.25", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Maestro 3364923093037194",
        },
        {
            "date": "2019-07-12T08:11:47.735774",
            "description": "Перевод организации",
            "from": "Visa Gold 3589276410671603",
            "id": 633268359,
            "operationAmount": {"amount": "2631.44", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 96292138399386853355",
        },
        {
            "date": "2018-02-22T00:40:19.984219",
            "description": "Перевод организации",
            "from": "MasterCard 4956649687637418",
            "id": 988276204,
            "operationAmount": {"amount": "71771.90", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 90562872508279542248",
        },
        {
            "date": "2019-09-29T14:25:28.588059",
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "id": 888407131,
            "operationAmount": {"amount": "45849.53", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 46723050671868944961",
        },
        {
            "date": "2018-01-21T01:10:28.317704",
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "id": 634356296,
            "operationAmount": {"amount": "96900.90", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 79619011266276091215",
        },
        {
            "date": "2018-11-23T23:52:36.999661",
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "id": 34148726,
            "operationAmount": {"amount": "79428.73", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Maestro 8045769817179061",
        },
        {
            "date": "2019-01-15T17:58:27.064377",
            "description": "Перевод организации",
            "from": "Visa Platinum 2241653116508487",
            "id": 970724427,
            "operationAmount": {"amount": "90688.44", "currency": {"code": "USD", "name": "USD"}},
            "state": "CANCELED",
            "to": "Счет 26494285169417058486",
        },
        {
            "date": "2019-06-01T06:46:16.803326",
            "description": "Перевод с карты на счет",
            "from": "МИР 8201420097886664",
            "id": 104807525,
            "operationAmount": {"amount": "60888.63", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 35116633516390079956",
        },
        {
            "date": "2018-07-31T12:25:32.579413",
            "description": "Перевод организации",
            "from": "MasterCard 8532498887072395",
            "id": 550607912,
            "operationAmount": {"amount": "34380.08", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 44238164562083919420",
        },
        {
            "date": "2018-10-08T09:05:05.282282",
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 6527183396477720",
            "id": 608117766,
            "operationAmount": {"amount": "77302.31", "currency": {"code": "USD", "name": "USD"}},
            "state": "CANCELED",
            "to": "Счет 38573816654581789611",
        },
        {
            "date": "2019-04-11T23:10:21.514616",
            "description": "Перевод с карты на карту",
            "from": "МИР 8193813157568899",
            "id": 484201274,
            "operationAmount": {"amount": "62621.51", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "МИР 9425591958944146",
        },
        {
            "date": "2018-12-29T21:45:18.495053",
            "description": "Перевод организации",
            "from": "Счет 77977573135347241529",
            "id": 547682597,
            "operationAmount": {"amount": "66263.93", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 33062909508148771891",
        },
        {
            "date": "2019-06-14T19:37:49.044089",
            "description": "Перевод со счета на счет",
            "from": "Счет 73222753239048295679",
            "id": 811920303,
            "operationAmount": {"amount": "63150.74", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 78544755774551298747",
        },
        {
            "date": "2019-10-30T01:49:52.939296",
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "id": 509645757,
            "operationAmount": {"amount": "23036.03", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 48943806953649539453",
        },
        {
            "date": "2019-11-05T12:04:13.781725",
            "description": "Открытие вклада",
            "id": 801684332,
            "operationAmount": {"amount": "21344.35", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 77613226829885488381",
        },
        {
            "date": "2019-08-08T21:58:06.688541",
            "description": "Перевод организации",
            "from": "Счет 99668626339273709694",
            "id": 122284694,
            "operationAmount": {"amount": "98657.83", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 27219929444683698245",
        },
        {
            "date": "2019-11-19T09:22:25.899614",
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "id": 154927927,
            "operationAmount": {"amount": "30153.72", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 43241152692663622869",
        },
        {
            "date": "2018-06-04T06:59:55.424356",
            "description": "Перевод организации",
            "from": "Счет 54883981902864782073",
            "id": 743628025,
            "operationAmount": {"amount": "978.31", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 61834060137088759145",
        },
        {
            "date": "2018-10-15T08:05:34.061711",
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1435442169918409",
            "id": 743278119,
            "operationAmount": {"amount": "51203.12", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Maestro 7452400219469235",
        },
        {
            "date": "2019-02-14T03:09:23.006652",
            "description": "Перевод организации",
            "from": "Visa Classic 6216537926639975",
            "id": 871921546,
            "operationAmount": {"amount": "47022.09", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 67667879435628279708",
        },
        {
            "date": "2018-03-09T02:11:01.339352",
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 7022985698476865",
            "id": 373912477,
            "operationAmount": {"amount": "33249.01", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 60979028617970883410",
        },
        {
            "date": "2018-11-08T08:21:45.902633",
            "description": "Перевод организации",
            "from": "Счет 75743795418434298755",
            "id": 720751477,
            "operationAmount": {"amount": "16872.46", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 80785963509390811744",
        },
        {
            "date": "2019-08-15T01:48:10.042554",
            "description": "Перевод организации",
            "from": "Счет 65298957349197687907",
            "id": 949194534,
            "operationAmount": {"amount": "31222.43", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 38784565940893479418",
        },
        {
            "date": "2018-01-23T01:48:30.477053",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 3414396880443483",
            "id": 260972664,
            "operationAmount": {"amount": "2974.30", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Gold 2684274847577419",
        },
        {
            "date": "2018-01-13T13:00:58.458625",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 8906171742833215",
            "id": 317987878,
            "operationAmount": {"amount": "55985.82", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 6086997013848217",
        },
        {
            "date": "2018-12-18T17:07:09.800800",
            "description": "Перевод со счета на счет",
            "from": "Счет 86675623828180311969",
            "id": 72122709,
            "operationAmount": {"amount": "19683.25", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 15351391408911677994",
        },
        {
            "date": "2019-07-08T00:08:32.986663",
            "description": "Перевод со счета на счет",
            "from": "Счет 38427597486442637521",
            "id": 242885401,
            "operationAmount": {"amount": "10083.68", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 83889757415570699323",
        },
        {
            "date": "2018-02-06T06:42:02.219233",
            "description": "Перевод организации",
            "from": "MasterCard 9175985085449563",
            "id": 286706711,
            "operationAmount": {"amount": "621.37", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 82781399328834147668",
        },
        {
            "date": "2019-06-21T12:34:06.351022",
            "description": "Открытие вклада",
            "id": 108066781,
            "operationAmount": {"amount": "25762.92", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 90817634362091276762",
        },
        {
            "date": "2019-03-03T03:13:18.622393",
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "id": 100392079,
            "operationAmount": {"amount": "44493.45", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 14073196441261107791",
        },
        {
            "date": "2018-08-25T02:58:18.764678",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 4040551273087672",
            "id": 51314762,
            "operationAmount": {"amount": "52245.30", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 7825450883088021",
        },
        {
            "date": "2018-07-15T18:44:13.346362",
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 9657499677062945",
            "id": 464419177,
            "operationAmount": {"amount": "71024.64", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 19213886662094884261",
        },
        {
            "date": "2019-12-03T04:27:03.427014",
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1796816785869527",
            "id": 560813069,
            "operationAmount": {"amount": "17628.50", "currency": {"code": "USD", "name": "USD"}},
            "state": "CANCELED",
            "to": "Visa Classic 7699855375169288",
        },
        {
            "date": "2019-08-04T20:17:25.443322",
            "description": "Перевод со счета на счет",
            "from": "Счет 33721541831646393763",
            "id": 894961746,
            "operationAmount": {"amount": "2523.44", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 68774571780974952778",
        },
        {
            "date": "2019-09-07T07:20:13.889610",
            "description": "Перевод с карты на карту",
            "from": "Maestro 4284341727554246",
            "id": 360577236,
            "operationAmount": {"amount": "18536.73", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "МИР 1582474475547301",
        },
        {
            "date": "2018-08-06T16:22:54.643491",
            "description": "Открытие вклада",
            "id": 285353808,
            "operationAmount": {"amount": "82946.19", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 12189246980267075758",
        },
        {
            "date": "2019-05-07T01:32:37.142797",
            "description": "Перевод с карты на карту",
            "from": "МИР 4878656375033856",
            "id": 416017997,
            "operationAmount": {"amount": "29033.65", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Maestro 6890749237669619",
        },
        {
            "date": "2019-05-17T01:50:00.166954",
            "description": "Перевод с карты на карту",
            "from": "МИР 8021883699486544",
            "id": 556488059,
            "operationAmount": {"amount": "74604.56", "currency": {"code": "USD", "name": "USD"}},
            "state": "CANCELED",
            "to": "Visa Gold 8702717057933248",
        },
        {
            "date": "2019-02-08T09:09:35.038506",
            "description": "Перевод организации",
            "from": "Счет 28429442875257789335",
            "id": 74897425,
            "operationAmount": {"amount": "62654.30", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 95473010446151855633",
        },
        {
            "date": "2019-06-16T22:17:01.825020",
            "description": "Перевод с карты на счет",
            "from": "Visa Platinum 8990850370884895",
            "id": 636137913,
            "operationAmount": {"amount": "24260.78", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 15574304810835774010",
        },
        {
            "date": "2018-05-04T03:29:30.253483",
            "description": "Перевод с карты на счет",
            "from": "MasterCard 3595832182277400",
            "id": 813238385,
            "operationAmount": {"amount": "22007.02", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 79697233246085035210",
        },
        {
            "date": "2019-03-29T10:57:20.635567",
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1203921041964079",
            "id": 854048120,
            "operationAmount": {"amount": "30234.99", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 34616199494072692721",
        },
        {
            "date": "2018-08-14T05:42:30.104666",
            "description": "Перевод со счета на счет",
            "from": "Счет 18125798580985711166",
            "id": 269462132,
            "operationAmount": {"amount": "19010.50", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 98841213648056852372",
        },
        {
            "date": "2019-02-14T17:38:09.910336",
            "description": "Перевод организации",
            "from": "Visa Classic 4610247282706784",
            "id": 692008409,
            "operationAmount": {"amount": "37044.95", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 63229171188548882700",
        },
        {
            "date": "2018-05-05T01:38:56.538074",
            "description": "Перевод с карты на счет",
            "from": "MasterCard 9454780748494532",
            "id": 431131847,
            "operationAmount": {"amount": "56071.02", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 51958934737718181351",
        },
        {
            "date": "2018-12-23T11:47:52.403285",
            "description": "Перевод с карты на карту",
            "from": "МИР 8665240839126074",
            "id": 15948212,
            "operationAmount": {"amount": "47408.20", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Maestro 3000704277834087",
        },
        {
            "date": "2019-12-07T06:17:14.634890",
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "id": 114832369,
            "operationAmount": {"amount": "48150.39", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 35158586384610753655",
        },
        {
            "date": "2019-04-18T11:22:18.800453",
            "description": "Открытие вклада",
            "id": 176798279,
            "operationAmount": {"amount": "73778.48", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 90417871337969064865",
        },
        {
            "date": "2019-11-13T17:38:04.800051",
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "id": 482520625,
            "operationAmount": {"amount": "62814.53", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 46765464282437878125",
        },
        {
            "date": "2019-06-30T15:11:53.136004",
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "id": 414894334,
            "operationAmount": {"amount": "95860.47", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 43475624104328495820",
        },
        {},
        {
            "date": "2019-04-19T12:02:30.129240",
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "id": 509552992,
            "operationAmount": {"amount": "81513.74", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "МИР 2052809263194182",
        },
        {
            "date": "2018-04-16T17:34:19.241289",
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "id": 596914981,
            "operationAmount": {"amount": "65169.27", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 97848259954268659635",
        },
        {
            "date": "2018-02-13T04:43:11.374324",
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "id": 200634844,
            "operationAmount": {"amount": "42210.20", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 45735917297559088682",
        },
        {
            "date": "2018-07-22T07:42:32.953324",
            "description": "Перевод организации",
            "from": "Счет 19628854383215954147",
            "id": 879660146,
            "operationAmount": {"amount": "92130.50", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 90887717138446397473",
        },
        {
            "date": "2018-02-03T07:16:28.366141",
            "description": "Открытие вклада",
            "id": 893507143,
            "operationAmount": {"amount": "90297.21", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 37653295304860108767",
        },
        {
            "date": "2018-08-17T03:57:28.607101",
            "description": "Перевод организации",
            "from": "Maestro 1913883747791351",
            "id": 710136990,
            "operationAmount": {"amount": "66906.45", "currency": {"code": "USD", "name": "USD"}},
            "state": "CANCELED",
            "to": "Счет 11492155674319392427",
        },
        {
            "date": "2019-02-12T00:08:07.524972",
            "description": "Перевод организации",
            "from": "Счет 72645194281643232984",
            "id": 390558607,
            "operationAmount": {"amount": "16796.95", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 95782287258966264115",
        },
        {
            "date": "2018-04-22T17:01:46.885252",
            "description": "Перевод организации",
            "from": "Visa Platinum 3530191547567121",
            "id": 902831954,
            "operationAmount": {"amount": "84732.61", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 46878338893256147528",
        },
        {
            "date": "2019-08-16T04:23:41.621065",
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8826230888662405",
            "id": 86608620,
            "operationAmount": {"amount": "6004.00", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 96119739109420349721",
        },
        {
            "date": "2018-07-06T22:32:10.495465",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 4062745111784804",
            "id": 232222017,
            "operationAmount": {"amount": "37160.27", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Maestro 8602249654751155",
        },
        {
            "date": "2018-09-27T14:26:24.629306",
            "description": "Перевод организации",
            "from": "Счет 23177857685058835559",
            "id": 280743947,
            "operationAmount": {"amount": "45653.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 56363465303962313778",
        },
        {
            "date": "2019-05-06T00:17:42.736209",
            "description": "Перевод со счета на счет",
            "from": "Счет 27921306202254867520",
            "id": 185048835,
            "operationAmount": {"amount": "74895.83", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 49884962711830774470",
        },
        {
            "date": "2019-02-27T03:59:25.921176",
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8847384717023026",
            "id": 422035015,
            "operationAmount": {"amount": "69311.35", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 85458008326755993377",
        },
        {
            "date": "2019-07-18T12:27:13.355343",
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "id": 917824439,
            "operationAmount": {"amount": "82139.20", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "МИР 2956603572573342",
        },
        {
            "date": "2018-06-08T16:14:59.936274",
            "description": "Перевод организации",
            "from": "Maestro 7552745726849311",
            "id": 121646999,
            "operationAmount": {"amount": "91121.62", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 34799481846914116850",
        },
        {
            "date": "2018-06-24T00:46:32.422648",
            "description": "Перевод организации",
            "from": "МИР 6381702861749111",
            "id": 816266176,
            "operationAmount": {"amount": "60030.73", "currency": {"code": "USD", "name": "USD"}},
            "state": "CANCELED",
            "to": "Счет 27804394774631586026",
        },
        {
            "date": "2019-09-06T00:48:01.081967",
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "id": 736942989,
            "operationAmount": {"amount": "6357.56", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 59986621134048778289",
        },
        {
            "date": "2018-06-20T03:59:34.851630",
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "id": 580054042,
            "operationAmount": {"amount": "96350.51", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 86655182730188443980",
        },
        {
            "date": "2019-08-19T16:30:41.967497",
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "id": 619287771,
            "operationAmount": {"amount": "81150.87", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 49304996510329747621",
        },
        {
            "date": "2018-12-22T02:02:49.564873",
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "id": 490100847,
            "operationAmount": {"amount": "56516.63", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "MasterCard 6783917276771847",
        },
        {
            "date": "2019-05-19T12:51:49.023880",
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "id": 179194306,
            "operationAmount": {"amount": "6381.58", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 58518872592028002662",
        },
        {
            "date": "2018-12-24T20:16:18.819037",
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "id": 27192367,
            "operationAmount": {"amount": "991.49", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 87448526688763159781",
        },
        {
            "date": "2018-03-09T23:57:37.537412",
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "id": 921286598,
            "operationAmount": {"amount": "25780.71", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 20735820461482021315",
        },
        {
            "date": "2019-07-15T11:47:40.496961",
            "description": "Открытие вклада",
            "id": 207126257,
            "operationAmount": {"amount": "92688.46", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 35737585785074382265",
        },
        {
            "date": "2019-01-05T00:52:30.108534",
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "id": 957763565,
            "operationAmount": {"amount": "87941.37", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 18889008294666828266",
        },
        {
            "date": "2019-07-13T18:51:29.313309",
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "id": 667307132,
            "operationAmount": {"amount": "97853.86", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 96527012349577388612",
        },
    ]


@pytest.fixture
def mock_csv_fixt():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


@pytest.fixture
def mock_excel_fixt():
    return [{"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]


@pytest.fixture
def csv_list_initial():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "4234093",
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": "23182",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": "30368",
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "366176",
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": "29482",
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5380041",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": "23789",
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "amount": "18588",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
            "description": "Перевод организации",
        },
        {
            "id": "5294458",
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "amount": "16836",
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5429839",
            "state": "EXECUTED",
            "date": "2023-06-23T19:46:34Z",
            "amount": "25261",
            "currency_name": "Hryvnia",
            "currency_code": "UAH",
            "from": "",
            "to": "Счет 76768135089446747029",
            "description": "Открытие вклада",
        },
        {
            "id": "3226899",
            "state": "EXECUTED",
            "date": "2023-04-17T09:21:15Z",
            "amount": "21680",
            "currency_name": "Koruna",
            "currency_code": "CZK",
            "from": "",
            "to": "Счет 88329674734590848775",
            "description": "Открытие вклада",
        },
        {
            "id": "3176764",
            "state": "CANCELED",
            "date": "2022-08-24T14:32:38Z",
            "amount": "16652",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Mastercard 8387037425051294",
            "to": "American Express 5556525473658852",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "1473389",
            "state": "EXECUTED",
            "date": "2023-08-30T00:58:36Z",
            "amount": "18420",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Mastercard 3093124722348405",
            "to": "American Express 6950002720800411",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def filter_by_curr_rub_csv():
    return [
        {
            "id": "4234093",
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": "23182",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "1473389",
            "state": "EXECUTED",
            "date": "2023-08-30T00:58:36Z",
            "amount": "18420",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Mastercard 3093124722348405",
            "to": "American Express 6950002720800411",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def filter_by_curr_rub_json():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


@pytest.fixture
def json_list_initial_short():
    return [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        },
        {
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "id": 41428829,
            "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 35383033474447895560",
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "id": 587085106,
            "operationAmount": {"amount": "48223.05", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 41421565395219882431",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def filter_by_description_list_initial():
    return [
        {
            "id": "4234093",
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": "23182",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "1473389",
            "state": "EXECUTED",
            "date": "2023-08-30T00:58:36Z",
            "amount": "18420",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Mastercard 3093124722348405",
            "to": "American Express 6950002720800411",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "212502",
            "state": "EXECUTED",
            "date": "2021-12-03T14:07:06Z",
            "amount": "21574",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 22246813624466689601",
            "to": "Счет 60148056083328746527",
            "description": "Перевод со счета на счет",
        },
        {
            "id": "3436241",
            "state": "EXECUTED",
            "date": "2023-10-20T21:00:39Z",
            "amount": "31741",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "American Express 5313948287096164",
            "to": "Discover 0329774489991288",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "3036684",
            "state": "EXECUTED",
            "date": "2022-03-25T01:54:48Z",
            "amount": "22818",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "American Express 5289343085624249",
            "to": "Счет 37876144219366357273",
            "description": "Перевод организации",
        },
    ]


@pytest.fixture
def filter_by_description_list_final():
    return [
        {
            "amount": "23182",
            "currency_code": "RUB",
            "currency_name": "Ruble",
            "date": "2021-07-08T07:31:21Z",
            "description": "Перевод с карты на карту",
            "from": "Visa 0773092093872450",
            "id": "4234093",
            "state": "EXECUTED",
            "to": "Discover 8602781449570491",
        },
        {
            "amount": "18420",
            "currency_code": "RUB",
            "currency_name": "Ruble",
            "date": "2023-08-30T00:58:36Z",
            "description": "Перевод с карты на карту",
            "from": "Mastercard 3093124722348405",
            "id": "1473389",
            "state": "EXECUTED",
            "to": "American Express 6950002720800411",
        },
        {
            "amount": "21574",
            "currency_code": "RUB",
            "currency_name": "Ruble",
            "date": "2021-12-03T14:07:06Z",
            "description": "Перевод со счета на счет",
            "from": "Счет 22246813624466689601",
            "id": "212502",
            "state": "EXECUTED",
            "to": "Счет 60148056083328746527",
        },
        {
            "amount": "31741",
            "currency_code": "RUB",
            "currency_name": "Ruble",
            "date": "2023-10-20T21:00:39Z",
            "description": "Перевод с карты на карту",
            "from": "American Express 5313948287096164",
            "id": "3436241",
            "state": "EXECUTED",
            "to": "Discover 0329774489991288",
        },
        {
            "amount": "22818",
            "currency_code": "RUB",
            "currency_name": "Ruble",
            "date": "2022-03-25T01:54:48Z",
            "description": "Перевод организации",
            "from": "American Express 5289343085624249",
            "id": "3036684",
            "state": "EXECUTED",
            "to": "Счет 37876144219366357273",
        },
    ]


@pytest.fixture
def list_of_types_fixt():
    return ["Открытие вклада", "Перевод с карты на карту", "Перевод организации", "Перевод со счета на счет"]


@pytest.fixture
def list_of_types_return_fixt():
    return {"Перевод с карты на карту": 3, "Перевод со счета на счет": 1, "Перевод организации": 1}


@pytest.fixture
def json_list_initial_short_2():
    return [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        }
    ]


@pytest.fixture
def mock_out_return_fixt():
    return (
        "26.08.2019 Перевод организации\n"
        " Maestro 1596 83** **** 5199 -> Счет **9589\n"
        " Сумма: 31957.58 руб.\n"
        "\n"
    )


@pytest.fixture
def csv_excel_list_initial_short_2():
    return [
        {
            "amount": "22818",
            "currency_code": "RUB",
            "currency_name": "Ruble",
            "date": "2022-03-25T01:54:48Z",
            "description": "Перевод организации",
            "from": "American Express 5289343085624249",
            "id": "3036684",
            "state": "EXECUTED",
            "to": "Счет 37876144219366357273",
        }
    ]


@pytest.fixture
def mock_out_return_fixt_2():
    return (
        "25.03.2022 Перевод организации\n"
        " American Express 5289 34** **** 4249 -> Счет **7273\n"
        " Сумма: 22818.0 RUB\n"
        "\n"
    )
