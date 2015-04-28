/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
   'use strict';

    angular.
        module('wildlife.portal.controllers').
        controller('FilterController', FilterController);

    FilterController.$inject = ['$scope', '$rootScope', '$location', 'FilterOptions', 'ViewingSiteService'];

    function FilterController($scope, $rootScope, $location, FilterOptions, ViewingSiteService) {

        $scope.facilities = [];
        $scope.animals = [];

        $scope.selectedAnimals = [];
        $scope.selectedFacilities = [];

        activate();

        function activate() {
            FilterOptions.getAnimals().then(getAnimalsSuccessFn, getAnimalsFailFn);

            function getAnimalsSuccessFn(data, status, headers, something) {
                $scope.animals = data.data;
            }

            function getAnimalsFailFn(data, status, headers, something) {
                console.log('Failed at getting animals');
            }

            FilterOptions.getFacilites().then(getFacilitiesSuccessFn, getFacilitiesFailFn);

            function getFacilitiesSuccessFn(data, status, headers, something) {
                $scope.facilities = data.data;
            }

            function getFacilitiesFailFn(data, status, headers, something) {
                console.log('Failed at getting facilities');
            }

            $scope.filter = function (){
                var animal = [];
                var facility = [];

                angular.forEach($scope.selectedAnimals, function(anim, index) {
                    animal.push(anim.id);
                });

                angular.forEach($scope.selectedFacilities, function(fac, index) {
                    facility.push(fac.id);
                });
                console.log($scope.selectedAnimals);
                ViewingSiteService.filterSites(facility, animal);
            }
        }
    }
})();