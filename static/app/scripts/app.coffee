
'use strict'

###*
 # @ngdoc overview
 # @name staticApp
 # @description
 # # staticApp
 #
 # Main module of the application.
###
angular
  .module('staticApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'monospaced.qrcode',
    'restangular',
    'ui.bootstrap'
  ])
  .config ($routeProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when '/about',
        templateUrl: 'views/about.html'
        controller: 'AboutCtrl'
      .when '/balance/:mpk',
        templateUrl: 'views/balance.html'
        controller: 'BalanceCtrl'
        resolve:
          balances:($route,Balances)->
            Balances.getList({mpk: $route.current.params.mpk})
      .otherwise
        redirectTo: '/'

  .config (RestangularProvider) ->
    # RestangularProvider.setBaseUrl 'http://api.cloudtrum.fabio.rueda.guru/api/'
    RestangularProvider.setBaseUrl 'http://localhost:8000/api/'

  .factory 'Balances' , (Restangular) ->
    Restangular.service 'balances'


    


