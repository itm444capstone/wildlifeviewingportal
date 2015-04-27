/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
   'use strict';

    angular.
        module('wildlife.portal.controllers').
        controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', '$rootScope'];

    function NavbarController ($scope, $rootScope) {
        $scope.isCollapsed = true;

        $scope.menuOptions = [
            {id: 0, name: 'Viewing Sites', url:'/'},
            {id: 1, name: 'Filter', url:'#!/filter'},
            {id: 2, name: 'Directions', url:'/'}
        ]

        $scope.navButtonClicked = function (id) {
            console.log(id);

            $rootScope.$broadcast('updateMode', id);
        }

        $scope.toggleMenuButtonClicked = function () {
            $scope.hideSidebar();
            $scope.isCollapsed = !$scope.isCollapsed;
        }

        $scope.$on('collapseMenu', function() {
            $scope.isCollapsed = true;
        });
    }
})();