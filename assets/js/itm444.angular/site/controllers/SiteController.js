/**
 * Created by brianjurgess on 4/27/15.
 */

(function (){

    angular.
        module('wildlife.site.controllers').
        controller('SiteController', SiteController);

    SiteController.$inject = ['$scope', '$rootScope', '$routeParams', 'SiteDetailService'];

    function SiteController($scope, $rootScope, $routeParams, SiteDetailService) {
        $scope.siteId = $routeParams.siteId;
        $scope.site = {};

        getSite();

        function getSite() {
            SiteDetailService.getSite($scope.siteId).then(getSiteSuccessFn, getSiteFailFn);

            function getSiteSuccessFn(data, status, headers, config) {
                $scope.site = data.data;
            }

            function getSiteFailFn(data, status, headers, config) {
                console.log("failed");
            }
        }
    }
})();