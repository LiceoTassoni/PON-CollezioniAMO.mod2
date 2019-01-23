var m = require("mithril");

var CollectionObject = {
    curObj : {},
    loadNext : function() {
        return m.request({
            method : "GET",
            url : "http://localhost:8088/fetch"
        }).then(function(result){
            CollectionObject.curObj = result;
        });
    }
};

module.exports = CollectionObject;
