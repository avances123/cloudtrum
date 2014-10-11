'use strict'

###*
 # @ngdoc function
 # @name staticApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the staticApp
###
angular.module('staticApp')
  .controller 'BalanceCtrl', ($scope,$log,$routeParams,balances,$location) ->
    $scope.alerts = []
    $scope.mpk = $routeParams.mpk
    $scope.balances = balances


    # Listeners
    $scope.$watchCollection 'balances', (newNames, oldNames) ->
        $scope.total_balance = 0
        angular.forEach newNames, (value, key) ->
            $scope.total_balance += value.balance            



    $scope.$on "$routeChangeError", (event, current, previous, rejection) ->
        #$log.error "Balance",event, current, previous, rejection
        $location.path('/')


    # Filtro para ver si es mayor que cero
    $scope.greaterThan = (prop, val) ->
        (item) ->
            return true if item[prop] > val

