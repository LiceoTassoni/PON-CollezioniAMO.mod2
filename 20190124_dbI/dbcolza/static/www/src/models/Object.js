var m = require("mithril");

var CollectionObject = {
    curObj : {},
    loadNext : function() {
        return m.request({
            method : "GET",
            url : "http://localhost:8088/getnext"
        }).then(function(result){
            CollectionObject.curObj = result.data;
        });
    }
};

module.exports = CollectionObject;
