app.controller("subscriptionCtrl", function($scope, $http, $window, $location, $sce, $timeout, store, config) {

    $scope.data = {}

    $scope.init = function(req, res) {

        alert("category");
    }

    var check = this;
    check.islogin = function(req, res) {
        var islogin = localStorage.getItem('islogin');
        $scope.name = localStorage.getItem('name');
        $scope.customerId = localStorage.getItem('customerId');
        $scope.org_id = localStorage.getItem('org_id');
        $scope.portfolio = {};
        $scope.portfolio.customerId = $scope.customerId;
        console.log(islogin); // gettin
        if (islogin == '1') {} else {
            console.log("we aere in the else loop. debug moere.. ")
            location.href = 'index.html';
        }
        return true;

    }


    $scope.list = function(req, res) {
        $scope.checklogin = check.islogin();
        if ($scope.checklogin == 1) {
            console.log("login successful ");
            $http.get(config.baseurl + "subscription/")
                .success(function(res) {
                    if (res.status == "false") {} else {
                        $scope.dataset = res.data;
                        console.log("Plan: ", $scope.dataset);
                    }
                })
                .error(function() {});
        }

    };

    $scope.tradesignallist = function(tradeSignalId) {
        localStorage.setItem('tradeSignalId', tradeSignalId); // setting
        location.href = "trade-signal-edit.html";
    };



    $scope.redirect = function() {
        //console.log("redirect");
        location.href = "index.html";
    };

    $scope.logout = function(req, res) {
        localStorage.removeItem("islogin");
        location.href = 'index.html';
    }



    $scope.add = function(req, res) {

        console.log($scope.data);

        if (typeof $scope.data.id == 'undefined') {
            alert($scope.data);

            $http.post(config.baseurl + 'subscription/', $scope.data)
                .success(function(res) {
                    if (res.status == 'false') {} else {
                        $scope.response = res.data;
                        console.log('message: ', $scope.response);
                        window.location.reload();
                    }
                }).error(function() {});

        } else {

            console.log($scope.data);
            $http.patch(config.baseurl + 'subscription/', $scope.data)
                .success(function(res) {
                    if (res.status == 'false') {} else {
                        $scope.response = res.data;
                        console.log('message: ', $scope.response);
                        window.location.reload();
                    }
                }).error(function() {});
        }


    }

    //orderCtrl ends

    $scope.update = function(id) {
        $http.get(config.baseurl + 'subscription/' + id)
            .success(function(res) {
                if (res.status == 'false') {} else {
                    $scope.data = res.data;
                    console.log('data: ', $scope.data);
                }
            }).error(function() {});
    }

    $scope.delete = function(id) {
        console.log("Delete clicked");
        $http.delete(config.baseurl + 'subscription/' + id + '/')
            .success(function(res) {
                if (res.status == 'false') {} else {
                    $scope.response = res.data;
                    console.log('data: ', $scope.response);
                }
            }).error(function() {});
        $window.location.reload();
    }




    $scope.logout = function(req, res) {
        localStorage.removeItem("islogin");
        location.href = 'index.html';
    }

    $scope.updateattachment = function() {
        console.log('yes');
        var img = new Image();
        var newfile = document.getElementById("file_browse").files[0];
        alert(newfile);
        var fileDisplayArea = document.getElementById('fileDisplayArea');
        var imageType = /image.*/;
        if (newfile.type.match(imageType)) {
            var oFReader = new FileReader();
            oFReader.onload = function(oFREvent) {
                $scope.data.thumbnail = document.getElementById("file_browse").files[0].name;
                console.log($scope.data.thumbnail);
                $scope.data.thumbnailimage = oFReader.result;
                console.log($scope.data.thumbnailimage);
                $scope.$apply();

            };
            oFReader.readAsDataURL(newfile);
            console.log($scope.data);
        } else {
            $scope.item.item_imagename = '';
            $scope.item.item_image = '';
        }
    };


});