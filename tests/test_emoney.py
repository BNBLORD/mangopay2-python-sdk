# -*- coding: utf-8 -*-
from tests import settings
from .resources import EMoney
from .test_base import BaseTest

import responses

class EMoneyTest(BaseTest):
    @responses.activate
    def test_retrieve_emoney(self):
        self.mock_legal_user()

        self.register_mock([
            {
                'method': responses.GET,
                'url': settings.MANGOPAY_API_SANDBOX_URL+settings.MANGOPAY_CLIENT_ID+'/users/64718764/emoney/',
                'body': {
                    "UserId": 64718764,
                    "CreditedEMoney": {
                        "Currency": "EUR",
                        "Amount": 0
                    },
                    "DebitedEMoney": {
                        "Currency": "EUR",
                        "Amount": 0
                    }
                },
                'status': 200,
                'match_querystring': True
            }])

        user_emoney = self.legal_user.get_emoney()
        self.assertIsNotNone(user_emoney.credited_emoney)
        self.assertIsNotNone(user_emoney.debited_emoney)
        self.assertIsInstance(user_emoney, EMoney)
