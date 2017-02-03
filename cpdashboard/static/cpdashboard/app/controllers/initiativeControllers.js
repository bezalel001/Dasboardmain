(function () {
    'use strict';
    angular
    .module('cpdApp')
    .controller('initiativesController', initiativesController);

    initiativesController.$inject = ['$scope', 'Initiatives'];
    function initiativesController($scope, Initiatives) {
        $scope.initiatives = Initiatives.query();
    }
    $scope.initiative = $scope.initiatives[0];

})();