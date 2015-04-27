/**
 * Created by brianjurgess on 4/26/15.
 */

(function () {
    angular.
        module('wildlife.portal.services').
        service('ViewingSiteService', ViewingSiteService);

    ViewingSiteService.$inject = ['$http', '$rootScope'];

    function ViewingSiteService ($http, $rootScope) {
        var ViewingSiteService = {
            getAllSites: getAllSites,
            filterSites: filterSites,
            availableSites: []
        };

        return ViewingSiteService;

        function getAllSites() {
            $http.get("/api/sites/").then(getAllSitesSuccessFn, getAllSitesFailFn);

            function getAllSitesSuccessFn(data, status, headers, config) {
                ViewingSiteService.availableSites = data.data;

                $rootScope.$broadcast('updateGraphics');
                $rootScope.$broadcast('updateSidebar');
            }

            function getAllSitesFailFn(data, status, headers, config) {
                console.log("Failed at getting all sites");
            }
        };

        function filterSites(facilities, animals) {
            var url = "/api/sites/?";
            if (facilities.length > 0) {
                var facilityUrl = "facilities=";
                facilityUrl += facilities.join(',');
                facilityUrl += '&';

                url += facilityUrl;
            }

            if (animals.length > 0) {
                var animalUrl = "animals=";
                animalUrl += animals.join(',');

                url += animalUrl;
            }

            $http.get(url).then(filterSitesSuccessFn, filterSitesFailFn);

            function filterSitesSuccessFn(data, status, headers, config) {
                ViewingSiteService.availableSites = data.data;

                $rootScope.$broadcast('updateGraphics');
                $rootScope.$broadcast('updateSidebar');
            }

            function filterSitesFailFn(data, status, headers, config) {
                console.log("Failed at filtering sites");
            }
        }
    }
})();