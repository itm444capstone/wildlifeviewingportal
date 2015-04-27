/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
    'use strict';

    angular.
        module('wildlife.portal.controllers').
        controller('SideBarController', SideBarController);

    SideBarController.$inject = ['$location', '$scope', '$rootScope', 'ViewingSiteService'];

    function SideBarController ($location, $scope, $rootScope, ViewingSiteService) {
        $scope.pageSize = 20;
        $scope.currentPage = 1;
        $scope.totalItems = ViewingSiteService.availableSites.length;
        $scope.itemsPerPage = 20;
        $scope.template = "/static/js/itm444.angular/portal/templates/sitelist.html";

        $scope.$on('updateSidebar', function (event, args) {
            console.log('in UpdateSidebar');
            //$scope.getCurrentPage();
            $scope.totalItems = ViewingSiteService.length;
            $scope.items = ViewingSiteService.availableSites;

            updateTemplate(0);
        });

        $scope.$on('updateMode', function (event, args) {
            updateTemplateAndOpenSideMenu(args);
        });

        function updateTemplateAndOpenSideMenu(args) {
            console.log(args);

            if (args == 0) {
                $scope.template = "/static/js/itm444.angular/portal/templates/sitelist.html";
            } else if (args == 1) {
                $scope.template = "/static/js/itm444.angular/portal/templates/filter.html";
            } else if (args == 2) {
                $scope.template = "";
            }
            $scope.setMode(args);
            $scope.showSidebar(args);
        }

        function updateTemplate(args) {
            if (args == 0) {
                $scope.template = "/static/js/itm444.angular/portal/templates/sitelist.html";
            } else if (args == 1) {
                $scope.template = "/static/js/itm444.angular/portal/templates/filter.html";
            } else if (args == 2) {
                $scope.template = "";
            }

            $scope.setMode(args);
            $scope.hideSidebar(args);
        }

        $scope.centerAt = function(n) {

            $rootScope.$broadcast('updateCenter', {lat: n.latitude, lng:n.longitude});
        }
    }
})();