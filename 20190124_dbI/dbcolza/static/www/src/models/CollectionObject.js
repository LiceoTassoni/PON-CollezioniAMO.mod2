var m = require("mithril");

var CollectionObject = {
    curObj : {},
    loadNext : function() {
        return m.request({
            method : "GET",
            url : "http://192.168.2.127:8088/fetch"
        }).then(function(result){
            CollectionObject.curObj = result;
        });
    },
    saveData : function(pData){
        return m.request({
            method : "POST",
            url : "http://192.168.2.127:8088/save",
            data : pData
        }).then(function() {
            CollectionObject.loadNext();
            return 0;
        });
    },
};

module.exports = CollectionObject;
