/**
 * Created by brianjurgess on 4/27/15.
 */

(function () {
    angular.
        module('wildlife.site.services').
        service('SiteDetailService', SiteDetailService);

    SiteDetailService.$inject = ['$http'];

    function SiteDetailService($http) {
        var SiteService = {
            getSite: getSite
        };

        return SiteService;

        function getSite(id) {
            var url = "/api/sites/" + id + '/';
            return $http.get(url);
        }
    }
})();