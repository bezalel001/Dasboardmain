(function () {
    'use strict';
    var initiativeServices = angular.module('initiativeServices', ['ngResource']);

    initiativeServices.factory('Initiatives', ['$resource',
      function ($resource) {
          return $resource('/cpdashboard/inits/?format=json', {}, {
              query: { method: 'GET', params: {}, isArray: true }
          });
      }]);

})();

