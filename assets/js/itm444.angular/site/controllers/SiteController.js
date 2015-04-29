/**
 * Created by brianjurgess on 4/27/15.
 */

(function (){

    angular.
        module('wildlife.site.controllers').
        controller('SiteController', SiteController);

    SiteController.$inject = ['$scope', '$rootScope', '$sce', '$routeParams', 'SiteDetailService'];

    function SiteController($scope, $rootScope, $sce, $routeParams, SiteDetailService) {
        $scope.siteId = $routeParams.siteId;
        $scope.site = {};
        $scope.alerts = [];

        $scope.deliberatelyTrustUnsafeHtml = function () {
            return $sce.trustAsHtml($scope.site.description);
        }

        getSite();

        function getSite() {
            SiteDetailService.getSite($scope.siteId).then(getSiteSuccessFn, getSiteFailFn);

            function getSiteSuccessFn(data, status, headers, config) {
                $scope.site = data.data;

                angular.forEach($scope.site.alerts, function(alert, index) {
                   var temp = {
                       title: alert.title
                   };

                    switch (alert.level) {
                        case 0:
                            temp.type = 'success';
                            break;
                        case 1:
                            temp.type = 'warning';
                            break;
                        case 2:
                            temp.type = 'danger';
                            break;
                    };
                    $scope.alerts.push(temp);
                });
            }

            function getSiteFailFn(data, status, headers, config) {
                console.log("failed");
            }

            $scope.closeAlert = function(index) {
                $scope.alerts.splice(index,1);
            }
        }
    }
})();