/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
    'use strict';

    angular.
        module('wildlife.portal.services').
        service('FilterOptions', FilterOptions);

    FilterOptions.$inject = ['$http'];

    function FilterOptions($http) {
        var FilterOptions = {
            getFacilites: getFacilities,
            getAnimals: getAnimals
        };

        return FilterOptions;

        function getFacilities() {
            return $http.get('/api/facilities/');
        }

        function getAnimals() {
            return $http.get('/api/animals/');
        }
    }
})();