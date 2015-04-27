/**
 * Created by brianjurgess on 4/26/15.
 */
(function() {
    'use strict'

    angular.module('wildlife.portal', [
        'wildlife.portal.controllers',
        'wildlife.portal.services'
    ]);


    angular.module('wildlife.portal.controllers', ['esri.map']);
    angular.module('wildlife.portal.services', []);
})();