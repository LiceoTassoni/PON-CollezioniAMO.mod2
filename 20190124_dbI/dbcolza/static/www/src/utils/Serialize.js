/*
 * function to serialize Form Data, because IE and Edge have poor
 * support for FormData objects
 * TODO: add support for multiple identical keys
 */

var serializeForm = function(formElement) {
    var chNd = formElement.elements,
        outpObj = {},
        group = 0;
    outpObj.fd = new FormData();

    for (var i = 0; i < chNd.length; i++) {
        var attTp = chNd[i].getAttribute("type"),
            attName = chNd[i].getAttribute("name");
        if (chNd[i].tagName === "INPUT") {
            if ((attTp === "text") || (attTp === "hidden")) {
                outpObj.fd.append(attName, chNd[i].value);
                outpObj[attName] = chNd[i].value;
            }
            if ((attTp === "radio") && (chNd[i].checked)) {
                outpObj.fd.append(attName, chNd[i].value);
                outpObj[attName] = chNd[i].value;
            }
            if ((attTp === "checkbox") && (chNd[i].checked)) {
                group = group + Math.pow(2, parseInt(chNd[i].value));
                outpObj.fd.append("gruppo", group);
                outpObj["gruppo"] = group;
            }
        }
        if (chNd[i].tagName === "SELECT") {
            outpObj.fd.append(attName, chNd[i].value);
            outpObj[attName] = chNd[i].value;
        }
        if (chNd[i].tagName === "TEXTAREA") {
            outpObj.fd.append(attName, chNd[i].value);
            outpObj[attName] = chNd[i].value;
        }
    }

    return outpObj;
};

module.exports = serializeForm;
