'use strict'

###*
 # @ngdoc function
 # @name staticApp.controller:AboutCtrl
 # @description
 # # AboutCtrl
 # Controller of the staticApp
###
angular.module('staticApp')
  .controller 'AboutCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]
