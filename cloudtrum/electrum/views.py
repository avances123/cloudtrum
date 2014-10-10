
from rest_framework import generics
from rest_framework.response import Response
from pybitcointools import *
from blockr.api import Api


coin = Api('Bitcoin')


class BalanceList(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):

        mpk = request.GET.get('mpk') 
        keys = []
        for i in range(20):
            keys.append(pubkey_to_address(electrum_pubkey(mpk,i,0)))

        balances = coin.address_balance(','.join(keys))
        return Response({
            'balances': balances
            })



