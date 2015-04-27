/**
 * Created by brianjurgess on 4/26/15.
 */

(function (){
    'use strict';

    angular.module('wildlife', [
        'ui.bootstrap',
        'wildlife.config',
        'wildlife.routes',
        'wildlife.portal',
        'wildlife.site'
    ]);

    angular.module('wildlife.routes', ['ngRoute']);
    angular.module('wildlife.config', []);
})();