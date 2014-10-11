'use strict'

###*
 # @ngdoc function
 # @name staticApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the staticApp
###
angular.module('staticApp')
  .controller 'MainCtrl', ($scope,$log,Balances,$location) ->
    $scope.alerts = []
    $scope.mpk = "3d3d5201021c586109549f5868ca441c65ea73800814186124020ff5043b35a75ecdb5ba4a3797f76a93f429aed1402ba40564c6045f5f41c719247236663697"
    $scope.new_mpk = (mpk) ->
        $location.path('/balance/' + mpk)






