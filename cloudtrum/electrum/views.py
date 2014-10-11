
from rest_framework import generics
from rest_framework.response import Response
from pybitcointools import *
from blockr.api import Api
from rest_framework import status
from rest_framework_extensions.cache.decorators import (cache_response)


coin = Api('Bitcoin')

def copyf(data):
    return filter(lambda x: "balance" in x.keys() and x["balance"] > 0, data)


class BalanceList(generics.ListAPIView):
    
    @cache_response(60 * 10)
    def get(self, request, *args, **kwargs):

        mpk = request.GET.get('mpk') 
        balances = []
        try:
            for x in [0,1]:
                keys = []
                for i in xrange(0,20):
                    keys.append(pubkey_to_address(electrum_pubkey(mpk,i,x)))
                    
                balances.extend(coin.address_balance(','.join(keys)).get('data'))


                keys = []
                for i in xrange(20,40):
                    keys.append(pubkey_to_address(electrum_pubkey(mpk,i,x)))
                    
                balances.extend(coin.address_balance(','.join(keys)).get('data'))
        except Exception, e:
            return Response({'msg':str(e)},status=status.HTTP_400_BAD_REQUEST)

        return Response(copyf(balances))



