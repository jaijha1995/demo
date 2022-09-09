var app = angular.module('website', ['angular-storage', 'angularPayments']);
app.config(['storeProvider', function(storeProvider) {
    storeProvider.setStore('sessionStorage');

app.controller('myCtrl', function($scope, $http) {
    $http.get("http://localhost:9009")
      .then(function(response) {
        $scope.result = response.data;
        console.log("OK:", response.data);
    }).catch(function(response) {
        console.log("ERROR:", response);
    });
});

}]);