/**
 * Created by brianjurgess on 4/27/15.
 */
(function(angular) {
    'use strict';

    angular.module('esri.map').directive('esriDirections', function ($document, $q) {
        return {
            priority: -10,
            scope:{},
            replace: true,
            // require the esriMap controller
            // you can access these controllers in the link function
            require:['^esriMap'],
            link: function(scope, element, attrs, controllers) {
                var mapController = controllers[0];
                var targetId = attrs.targetId || attrs.id;
                var directionsDeferred = $q.defer();

                require(['esri/dijit/Directions', 'dijit/registry'], function (Directions, registry) {
                   mapController.getMap().then(function(map) {
                       var opts = {
                           map: map
                       };

                       var directions = registry.byId(targetId);
                       if (directions) {
                           directions.destroy();
                       }

                       directions = new Directions(opts, targetId);
                       directions.startup();

                       scope.$on('destroy', function() {
                           directions.destroy();
                       });
                   });
                });
            }
        }
    })
})(angular);