/**
 * Created by brianjurgess on 4/26/15.
 */

(function (){
    'use strict';

    angular
        .module('wildlife.portal.controllers')
        .controller('MapController', MapController);

    MapController.$inject = ['$location', '$scope', 'ViewingSiteService', 'esriRegistry', '$rootScope'];

    function MapController($location, $scope, ViewingSiteService, esriRegistry, $rootScope) {
        $scope.map = {
            center: {
                lng: -84.5467,
                lat: 42.7336
            },
            zoom: 8
        };

        $scope.mapLoaded = function(map) {
            console.log(map);

            map.resize();
            map.reposition();

            require(["esri/urlUtils"], function(urlUtils) {
                urlUtils.addProxyRule({
                    urlPrefix: "http://utility.arcgis.com/usrsvcs/servers/f9ae150a65714083b53ced8d159a7432/rest/services/World/Route/NAServer/Route_World",
                    proxyUrl: "/sproxy/"
                });
            });

            getAllSites();
        };

        $scope.getAllSites = getAllSites;

        $scope.$on('updateGraphics', function(event, args) {
            updateMapGraphics();
        });

        $scope.$on('updateCenter', function(event, args) {
            $scope.hideSidebar();
            $scope.map.center.lat = args.lat;
            $scope.map.center.lng = args.lng;
        });

        function getAllSites() {
            ViewingSiteService.getAllSites();
        }

        function updateMapGraphics() {
            esriRegistry.get('mainMap').then(function (map) {
                var infoTemplate = null;
                require(['esri/InfoTemplate'], function (InfoTemplate) {
                    infoTemplate = new InfoTemplate();
                    infoTemplate.setTitle("${name}");
                    infoTemplate.setContent(
                        "<b>Owner: </b>${owner}<br />" +
                            "<b>Telephone: </b>${telephone}<br />" +
                            "<a href='#/site/${id}'>View More</a>"
                    );
                });

                map.graphics.setInfoTemplate(infoTemplate);
               map.graphics.clear();
                angular.forEach(ViewingSiteService.availableSites, function(value, key) {
                   var attributes = {
                       id: value['id'],
                       name: value['name'],
                       description: value['description'],
                       owner: value['owner'],
                       link: value['link'],
                       telephone: value['telephone']
                   };
                    var lat = value['latitude'];
                    var lng = value['longitude'];


                    require(['esri/graphic', 'esri/geometry/Point',
                    'esri/symbols/SimpleMarkerSymbol', 'esri/Color',
                    'esri/SpatialReference'], function(Graphic, Point,
                    SimpleMarkerSymbol, Color, SpatialReference) {
                        var marker = SimpleMarkerSymbol({
                            color: [0, 255, 0, 64],
                            size: 12,
                            outline: {
                                color: [0,0,0,255],
                                width: 1,
                                type: "esriSLS",
                                style: "esriSLSSolid"
                            }
                        });
                        var point = Point(lng, lat, new SpatialReference({wkid: 4326}));
                        var graphic = new Graphic(point, marker);
                        graphic.setAttributes(attributes);
                        map.graphics.add(graphic);
                    });
                });
            });
        }
    }
})();