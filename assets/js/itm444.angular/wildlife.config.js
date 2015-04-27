/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
   'use strict';

    angular
        .module('wildlife.config')
        .config(config);

    config.$inject = ['$locationProvider'];

    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        //$locationProvider.hashPrefix('!');
    }
})();