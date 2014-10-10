'use strict'

###*
 # @ngdoc function
 # @name staticApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the staticApp
###
angular.module('staticApp')
  .controller 'BalanceCtrl', ($scope,$log,$routeParams) ->
    $scope.alerts = []
    $scope.mpk = "3d3d5201021c586109549f5868ca441c65ea73800814186124020ff5043b35a75ecdb5ba4a3797f76a93f429aed1402ba40564c6045f5f41c719247236663697"
    $scope.new_mpk = (mpk) ->
        balances = Restangular.all 'balances'
        balances.getList({mpk: mpk}).then (bals) -> 
            $scope.balances = bals
        , (error) ->
            $scope.alerts.push 
                msg:error.data.msg
                type:"danger"


    $scope.$watchCollection 'balances', (newNames, oldNames) ->
        $scope.total_balance = 0
        angular.forEach newNames, (value, key) ->
            $scope.total_balance += value.balance            


    # Filtro para ver si es mayor que cero
    $scope.greaterThan = (prop, val) ->
        (item) ->
            return true if item[prop] > val