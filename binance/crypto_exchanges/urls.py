from django.urls import include, path

from crypto_exchanges.views import (CryptoExchangeCard2CryptoExchanges,
                                    CryptoExchangeCard2Wallet2CryptoExchanges,
                                    CryptoExchangeInternalExchanges,
                                    CryptoExchangeP2PExchanges,
                                    CryptoExchangesCard2CryptoExchanges,
                                    CryptoExchangesCard2Wallet2CryptoExchanges,
                                    CryptoExchangesInternalExchanges,
                                    CryptoExchangesP2PExchanges, all,
                                    binance_best_card_2_card_crypto_exchanges,
                                    binance_best_crypto_exchanges,
                                    binance_card_2_crypto_exchanges,
                                    binance_crypto, binance_fiat_crypto_list,
                                    binance_inter_exchanges_calculate,
                                    card_2_wallet_2_crypto, p2p_binance,
                                    CryptoExchangesBestPaymentChannelsExchanges,
                                    CryptoExchangeBestPaymentChannelsExchanges,
                                    IntraBanksCryptoExchangesCombinations,
                                    IntraBankCryptoExchangeCombinations)

app_name = 'crypto_exchanges'

urlpatterns = [
    path('crypto_exchanges/internal_crypto_exchanges/',
         CryptoExchangesInternalExchanges.as_view(),
         name='crypto_exchanges_internal_exchanges'),
    path('<str:crypto_exchange_name>/internal_crypto_exchanges/',
         CryptoExchangeInternalExchanges.as_view(),
         name='crypto_exchange_internal_exchanges'),
    path('crypto_exchanges/banks/p2p_exchanges/',
         CryptoExchangesP2PExchanges.as_view(),
         name='crypto_exchanges_p2p_exchanges'),
    path('<str:crypto_exchange_name>/<str:bank_name>/p2p_exchanges/',
         CryptoExchangeP2PExchanges.as_view(),
         name='crypto_exchange_p2p_exchanges'),
    path('crypto_exchanges/banks/card_2_wallet_2_crypto_exchanges/',
         CryptoExchangesCard2Wallet2CryptoExchanges.as_view(),
         name='crypto_exchanges_card_2_wallet_2_crypto_exchanges'),
    path('<str:crypto_exchange_name>/<str:bank_name>/'
         'card_2_wallet_2_crypto_exchanges/',
         CryptoExchangeCard2Wallet2CryptoExchanges.as_view(),
         name='crypto_exchange_card_2_wallet_2_crypto_exchanges'),
    path('crypto_exchanges/banks/card_2_crypto_exchanges/',
         CryptoExchangesCard2CryptoExchanges.as_view(),
         name='crypto_exchanges_card_2_crypto_exchanges'),
    path('<str:crypto_exchange_name>/<str:bank_name>/card_2_crypto_exchanges/',
         CryptoExchangeCard2CryptoExchanges.as_view(),
         name='crypto_exchange_card_2_crypto_exchanges'),
    path('crypto_exchanges/banks/best_payment_channels_exchanges/',
         CryptoExchangesBestPaymentChannelsExchanges.as_view(),
         name='crypto_exchanges_best_payment_channels_exchanges'),
    path('<str:crypto_exchange_name>/<str:bank_name>/'
         'best_payment_channels_exchanges/',
         CryptoExchangeBestPaymentChannelsExchanges.as_view(),
         name='crypto_exchange_best_payment_channels_exchanges'),
    path('crypto_exchanges/banks/intra_banks_exchanges_via_crypto_exchanges/',
         IntraBanksCryptoExchangesCombinations.as_view(),
         name='intra_banks_exchanges_via_crypto_exchanges_best_combinations'),
    path('<str:crypto_exchange_name>/<str:bank_name>/'
         'intra_banks_exchanges_via_crypto_exchanges/',
         IntraBankCryptoExchangeCombinations.as_view(),
         name='intra_bank_exchanges_via_crypto_exchange_best_combinations'),
    path('1/', p2p_binance, name="p2p_binance"),
    path('100/', binance_crypto, name="binance_crypto"),
    path('200/', card_2_wallet_2_crypto, name="binance_card_2_wallet_2_crypto"),
    path('300/', binance_fiat_crypto_list, name="binance_fiat_crypto_list"),
    path('400/', binance_card_2_crypto_exchanges,
         name="binance_card_2_crypto_exchanges"),
    path('500/', binance_best_crypto_exchanges,
         name="binance_best_crypto_exchanges"),
    path('600/', binance_best_card_2_card_crypto_exchanges,
         name="binance_best_card_2_card_crypto_exchanges"),
    path('700/', binance_inter_exchanges_calculate,
         name="binance_inter_exchanges_calculate"),
    path('1000/', all, name="all")
]
