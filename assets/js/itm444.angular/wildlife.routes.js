/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
    'use strict';

    angular
        .module('wildlife.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider.when('/site/:siteId', {
            controller: 'SiteController',
            controllerAs: 'wvp',
            templateUrl: '/static/js/itm444.angular/site/templates/site.html'
        }).when('/', {
            controller: 'IndexController',
            controllerAs: 'wvp',
            templateUrl: '/static/js/itm444.angular/portal/templates/index.html',
            action: "index.home"
        }).otherwise('/');
    }
})();