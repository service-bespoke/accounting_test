var invoice_item_row_counter = 1
var payment_item_row_counter = 1
var fuse_customers;




// ADDING INVOICE ROWS ===================================================
function add_invoice_item_row() {

    invoice_item_row_counter=$('#invoice-form-items-table-body >tr:last td')[0].innerText
    invoice_item_row_counter++;

    $('#invoice-form-items-table-body >tr:last').clone(true).insertAfter('#invoice-form-items-table-body >tr:last');
    $('#invoice-form-items-table-body >tr:last input').val('');

    $('#invoice-form-items-table-body >tr:last td')[0].innerHTML = invoice_item_row_counter
    update_amounts($('#invoice-form-items-table-body input[name=service-name]:last'));
    $('#invoice-form-items-table-body input[name=service-name]:last').focus();

}


function setup_invoice_rows() {
    $("#invoice-form-addrow").click(function (event) {
        event.preventDefault();
        add_invoice_item_row();
    });

}

// UPDATING INVOICE TOTALS ================================================

function update_invoice_totals() {
    // amount cgst
    service_total = 0
    billvat=0
    service_total = parseFloat($('input[name=bill-total]').val());
    billvat=service_total*0.05;
    $('input[name=bill-vat]').val(billvat.toFixed(2));
    service_grandtotal = service_total + parseFloat($('input[name=bill-vat]').val()) - parseFloat($('input[name=bill-discount]').val())
    $('input[name=bill-grandtotal').val(service_grandtotal.toFixed(2));

}


// AUTO CALCULATE ITEM AMOUNTS =============================================

function initialize_auto_calculation() {
    update_amounts($('#invoice-form-items-table-body input[name=service-name]:first'));
    $('input[name=service-rate],input[name=service-qty],input[name=bill-total],input[name=additional], input[name=bill-discount], input[name=bill-extra]').change(function () {
        update_amounts($(this));
    });
}

function update_amounts(element) {
    var test = element.parent().parent().find('input[name=service-name]').val();
    var rate = parseFloat(element.parent().parent().find('input[name=service-rate]').val());
    var qty = parseFloat(element.parent().parent().find('input[name=service-qty]').val());
    var test_amt;
    if (test == "") {
        test_amt = 0;
    } else {

        test_amt = rate * qty;
        console.log(test_amt)
    }
    console.log(test_amt)
    element.parent().parent().find('input[name=service-amount]').val(test_amt.toFixed(2));

    update_invoice_totals();

}


function update_voucher_amounts(element) {
    var total_amt=0;
    $('input[name=amount]').each(function () {
        console.log($(this).val())
        total_amt += parseFloat($(this).val());
    });
    $('input[name=total_amount]').val(total_amt.toFixed(2));

}



// item SEARCH ========================================================

var selected_item_input;

function item_result_to_domstr(result) {
    var domstr = "<div class='item-search-result' data-item='" + JSON.stringify(result) + "'>" +
        "<div>" + result['itemName'] + "</div>" +
        "<div>" + result['itemCode'] +"</div>"+
        "<div>" + result['make'] + "</div>" ;
    return domstr;
}

var testexist = false;

function item_result_click() {
    console.log("UPDATE THE FORM WITH SEARCH RESULT");
    item_data_json = JSON.parse($(this).attr('data-item'));

    $('input[name=test-code]').not(':last').each(function () {

        if ($(this).val() == item_data_json['code'] || $(this).val() == '') {
            testexist = true;
            console.log(testexist);
            return false;

        } else {
            testexist = false;
            console.log(testexist);

        }
    });

    if (!testexist) {
        selected_item_input.val(item_data_json['name']);

        selected_item_input.parent().parent().find('input[name=item_id]').val(item_data_json['id']);
        selected_item_input.parent().parent().find('input[name=itemCode]').val(item_data_json['itemCode']);
        selected_item_input.parent().parent().find('input[name=category]').val(item_data_json['category_id']);
        selected_item_input.parent().parent().find('input[name=unit]').val(item_data_json['unit_id']);
        selected_item_input.parent().parent().find('input[name=itemName]').val(item_data_json['itemName']);
        selected_item_input.parent().parent().find('input[name=description]').val(item_data_json['description']);
        selected_item_input.parent().parent().find('input[name=make]').val(item_data_json['make']);
        selected_item_input.parent().parent().find('input[name=location]').val(item_data_json['location']);
        selected_item_input.parent().parent().find('input[name=vat]').val(item_data_json['vat']);
        selected_item_input.parent().parent().find('input[name=is_vatInclusive]').val(item_data_json['is_vatInclusive']);
        $('#item_search_bar').hide();
        update_amounts($(selected_item_input));
    }
}

function initialize_fuse_item_search_bar() {
    console.log("INITIALIZING item SEARCH");

    $(".item_search_area").focusin(function () {
        console.log("DISPLAY item SEARCH");
        $("#item_search_bar").show();
        var input = $(this);
        selected_item_input = input;
        var val = input.val();
        update_item_search_bar(val);
    });

    $(document).bind('focusin click', function (e) {
        if ($(e.target).closest('#item_search_bar, .item_search_area').length) return;
        $('#item_search_bar').hide();
    });

    $(".item_search_input").on("input", function (e) {
        $("#item_search_bar").show();
        var input = $(this);
        var val = input.val();
        update_item_search_bar(val);
    });
}

function update_item_search_bar(search_string) {
    console.log("Update item search bar with query: " + search_string);
    results = fuse_items.search(search_string);
    console.log(results);
    $("#item_search_bar").empty();
    for (var i = 0; i < results.length; i++) {
        $("#item_search_bar").append(item_result_to_domstr(results[i]));
    }
    $('.item-search-result').click(item_result_click);
}


function initialize_fuse_items() {
    // fetch customer data
    $.getJSON("../items/get_item_json", function (data) {
        var fuse_item_options = {
            shouldSort: true,
            threshold: 0.6,
            location: 0,
            distance: 100,
            maxPatternLength: 32,
            minMatchCharLength: 1,
            keys: [
                "itemName",
                "itemCode",
                "description"
            ]
        };
        fuse_items = new Fuse(data, fuse_item_options);
        // initialize the search bar
        initialize_fuse_item_search_bar();
    });
}



// CUSTOMER SEARCH ========================================================

function customer_result_to_domstr(result) {
    var domstr = "<div class='customer-search-result' data-customer='" + JSON.stringify(result) + "'>" +
        "<div>" + result['customer_name'] + "</div>" +
        "<div>" + result['customer_address1'] + "</div>" +
        "<div>" + result['customer_phone1'] + "</div>" +
        "</div>";
    return domstr;
}

function customer_result_click() {
    console.log("UPDATE THE FORM WITH SEARCH RESULT");
    customer_data_json = JSON.parse($(this).attr('data-customer'));
    $('#customer_name').val(customer_data_json['customer_name']);
    $('#customer_address1').val(customer_data_json['customer_address1']);
    $('#customer_trn').val(customer_data_json['customer_trn']);
    $('#customer_phone').val(customer_data_json['customer_phone1']);
    $('#customer_id').val(customer_data_json['id']);
    $('#customer_search_bar').hide();
}

function initialize_fuse_customers_search_bar() {
    console.log("INITIALIZING CUSTOMER SEARCH");

    $(".customer_search_area").focusin(function () {
        $("#customer_search_bar").show();
        var input = $('.customer_search_input');
        var val = input.val();
        update_customer_search_bar(val);
    });

    $(document).bind('focusin click', function (e) {
        if ($(e.target).closest('#customer_search_bar, .customer_search_area').length) return;
        $('#customer_search_bar').hide();
    });

    $(".customer_search_input").on("input", function (e) {
        $("#customer_search_bar").show();
        var input = $(this);
        var val = input.val();
        update_customer_search_bar(val);
    });
}

function update_customer_search_bar(search_string) {
    console.log("Update customer search bar with query: " + search_string);
    results = fuse_customers.search(search_string);
    console.log(results);
    $("#customer_search_bar").empty();
    for (var i = 0; i < results.length; i++) {
        $("#customer_search_bar").append(customer_result_to_domstr(results[i]));
    }
    $('.customer-search-result').click(customer_result_click);
}


function initialize_fuse_customers() {
    // fetch customer data
    $.getJSON("/sales/get_customer_json", function (data) {
        var fuse_customer_options = {
            shouldSort: true,
            threshold: 0.6,
            location: 0,
            distance: 100,
            maxPatternLength: 32,
            minMatchCharLength: 1,
            keys: [
                "customer_name",
                "customer_phone1",
                "customer_address1",
            ]
        };
        fuse_customers = new Fuse(data, fuse_customer_options);
        console.log(fuse_customers)
        // initialize the search bar
        initialize_fuse_customers_search_bar();
    });
}


// SUPPLIER SEARCH ========================================================

function supplier_result_to_domstr(result) {
    var domstr = "<div class='supplier-search-result' data-supplier='" + JSON.stringify(result) + "'>" +
        "<div>" + result['supplier_name'] + "</div>" +
        "<div>" + result['supplier_code'] + "</div>" +
        "<div>" + result['supplier_address1'] + "</div>" +
        "</div>";
    return domstr;
}

function supplier_result_click() {
    console.log("UPDATE THE FORM WITH SEARCH RESULT");
    supplier_data_json = JSON.parse($(this).attr('data-supplier'));
    $('#supplier_name').val(supplier_data_json['supplier_name']);
    $('#id_batch').val(supplier_data_json['supplier_code']);
    $('#supplier_search_bar').hide();
}

function initialize_fuse_suppliers_search_bar() {
    console.log("INITIALIZING supplier SEARCH");

    $(".supplier_search_area").focusin(function () {
        $("#supplier_search_bar").show();
        var input = $('.supplier_search_input');
        var val = input.val();
        update_supplier_search_bar(val);
    });

    $(document).bind('focusin click', function (e) {
        if ($(e.target).closest('#supplier_search_bar, .supplier_search_area').length) return;
        $('#supplier_search_bar').hide();
    });

    $(".supplier_search_input").on("input", function (e) {
        $("#supplier_search_bar").show();
        console.log()
        var input = $(this);
        var val = input.val();
        update_supplier_search_bar(val);
    });
}

function update_supplier_search_bar(search_string) {
    console.log("Update supplier search bar with query: " + search_string);
    results = fuse_suppliers.search(search_string);
    // console.log(results);
    $("#supplier_search_bar").empty();
    for (var i = 0; i < results.length; i++) {
        $("#supplier_search_bar").append(supplier_result_to_domstr(results[i]));
    }
    $('.supplier-search-result').click(supplier_result_click);
}


function initialize_fuse_suppliers() {
    // fetch supplier data
    $.getJSON("/items/get_supplier_json", function (data) {
        var fuse_supplier_options = {
            shouldSort: true,
            threshold: 0.6,
            location: 0,
            distance: 100,
            maxPatternLength: 32,
            minMatchCharLength: 1,
            keys: [
                "supplier_name",
                "supplier_code",
                "supplier_address1",
            ]
        };
        fuse_suppliers = new Fuse(data, fuse_supplier_options);

        // initialize the search bar
        initialize_fuse_suppliers_search_bar();
    });
}


// START =============================================================

$(document).ready(function () {
    console.log("ready")

   

    $(".hiden-form").hide();
    // Initialize invoice row addition
    setup_invoice_rows();


    // Initialize customer search
    initialize_fuse_customers();

    // Initialize supplier search
    initialize_fuse_suppliers();

    // Initialize item search
    initialize_fuse_items();

    // Initialize auto calculation of amounts
    initialize_auto_calculation();


    $("input[name=amount]").change(function () {
        update_voucher_amounts($(this));
    });

    $("#id_default_value").change(function () {
        console.log("checked");
        $(".hiden-form").toggle();
    });

    // Show the invoice form
    $("#invoice-form")[0].hidden = false;
});



/* Prototyping
/* ========================================================================== */

(function (window, ElementPrototype, ArrayPrototype, polyfill) {
    function NodeList() {
        [polyfill]
    }
    NodeList.prototype.length = ArrayPrototype.length;

    ElementPrototype.matchesSelector = ElementPrototype.matchesSelector ||
        ElementPrototype.mozMatchesSelector ||
        ElementPrototype.msMatchesSelector ||
        ElementPrototype.oMatchesSelector ||
        ElementPrototype.webkitMatchesSelector ||
        function matchesSelector(selector) {
            return ArrayPrototype.indexOf.call(this.parentNode.querySelectorAll(selector), this) > -1;
        };

    ElementPrototype.ancestorQuerySelectorAll = ElementPrototype.ancestorQuerySelectorAll ||
        ElementPrototype.mozAncestorQuerySelectorAll ||
        ElementPrototype.msAncestorQuerySelectorAll ||
        ElementPrototype.oAncestorQuerySelectorAll ||
        ElementPrototype.webkitAncestorQuerySelectorAll ||
        function ancestorQuerySelectorAll(selector) {
            for (var cite = this, newNodeList = new NodeList; cite = cite.parentElement;) {
                if (cite.matchesSelector(selector)) ArrayPrototype.push.call(newNodeList, cite);
            }

            return newNodeList;
        };

    ElementPrototype.ancestorQuerySelector = ElementPrototype.ancestorQuerySelector ||
        ElementPrototype.mozAncestorQuerySelector ||
        ElementPrototype.msAncestorQuerySelector ||
        ElementPrototype.oAncestorQuerySelector ||
        ElementPrototype.webkitAncestorQuerySelector ||
        function ancestorQuerySelector(selector) {
            return this.ancestorQuerySelectorAll(selector)[0] || null;
        };
})(this, Element.prototype, Array.prototype);


function deleterow(e) {
    var element = e.target.querySelector('[contenteditable]'),
        row;
    element && e.target != document.documentElement && e.target != document.body && element.focus();
    console.log(e.target.ancestorQuerySelector('tr'))
    row = e.target.ancestorQuerySelector('tr');

    row.parentNode.removeChild(row);
    initialize_auto_calculation();

}