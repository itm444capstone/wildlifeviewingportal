/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
   'use strict';

    angular.
        module('wildlife.portal.controllers').
        controller('IndexController', IndexController);

    IndexController.$inject = ['$location', '$scope', '$window', '$route', '$routeParams', 'ViewingSiteService'];

    function IndexController($location, $scope, $window, $route, $routeParams, ViewingSiteService) {
        $scope.sites = [];
        $scope.mode = 0;
        $scope.small = false;
        $scope.showsidebar = false;
        console.log($routeParams);
        $scope.setSite = function setSite(array) {
            $scope.sites = array;
            console.log($scope.sites);
        };

        $scope.setMode = function (arg) {
            $scope.mode = arg;
        };

        $scope.showSidebar = function (arg) {
            $scope.showsidebar = true;
            $scope.$broadcast('collapseMenu');
        };

        $scope.hideSidebar = function () {
            $scope.showsidebar = false;
        }

        $scope.$on('$routeChangeSuccess', function ($currentRoute, $previousRoute) {
            console.log($currentRoute);
        });

    }
})();