'use strict'

###*
 # @ngdoc function
 # @name staticApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the staticApp
###
angular.module('staticApp')
  .controller 'BalanceCtrl', ($scope,$log,$routeParams,balances) ->
    $scope.alerts = []
    $scope.mpk = $routeParams.mpk
    $scope.balances = balances


    $scope.$watchCollection 'balances', (newNames, oldNames) ->
        $scope.total_balance = 0
        angular.forEach newNames, (value, key) ->
            $scope.total_balance += value.balance            


    # Filtro para ver si es mayor que cero
    $scope.greaterThan = (prop, val) ->
        (item) ->
            return true if item[prop] > val