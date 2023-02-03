//net Price 
function changeadvance(e) {
    adv = parseFloat($('input.advanceprice' + e).val())
    value = parseFloat($('input.totalprice' + e).val().replace("₹", "").trim())
    if (adv) {
        value -= adv;
    }
    net = `₹ ${value}.00`
    $("input.netprice" + e).val(net);
}
// total price
function amountchange(part_id, challan_id) {
    var sum = 0;
    value = `₹ 0.00`;
    $('input.form-control.amount.challan' + challan_id).each(function() {
        if (this.value) {
            sum += parseFloat(this.value);
            value = `₹ ${sum}.00`;
        }
    });
    $("input.totalprice" + challan_id).val(value);
    changeadvance(challan_id);
}


// function calledit_parts(challan_no) {
//     var parti_no = $('.amount.challan' + challan_no).length;
//     editchallan_parts(parseInt(parti_no + 1), challan_no);
// }

function editchallan_parts(part_id, challan_no) {
    var max_fields = 15;
    part_no = part_id + 1;
    var wrapper = $(".input_fields_wrap" + challan_no);
    var add_button = $(".add_field_button" + challan_no);
    var x = 1;
    if (x < max_fields) {
        x++;
        $(wrapper).append('<div class="row editparts' + part_no + '"><div class ="col-md-3 col-sm-12"><div class= "form-group"><label>Particulars</label><input type= "text"class="form-control" id="uc-particulars-desc"></div></div><div class="col-md-2 col-sm-12"><div class= "form-group"><label>Size</label><input type="text" class="form-control" id="uc-size-desc"></div></div><div class="col-md-2 col-sm-12"><div class ="form-group"><label>Qty</label><input type="number" class="form-control qty' + part_no + '" onchange=raqchange(' + part_no + ',' + challan_no + ')  id="uc-qty-desc" value="0"></div></div ><div class="col-md-2 col-sm-12"><div class ="form-group"><label>Rate</label><input type="number" class="form-control rate' + part_no + '" onchange=raqchange(' + part_no + ',' + challan_no + ')  id="uc-rate-desc" value="0"></div></div ><div class="col-md-2 col-sm-12"><div class ="form-group"><label>Amount</label><input type="number" class="form-control amount challan' + challan_no + ' part' + part_no + '" onchange=amountchange(' + part_no + ',' + challan_no + ')  id="uc-amount-desc" disabled></div></div ><div class="col-md-1 col-sm-12"><button type="button" style="cursor:pointer;background-color:red;margin-top:30px;" class="remove_field' + challan_no + ' btn btn-info" onclick="editremove(' + String(part_no) + ',' + String(challan_no) + ')">X</button></div></div>');
        //add input box
    }
}

function editremove(part_no, challan_no) {
    $('.editparts' + part_no).remove();
    amountchange(part_no, challan_no);
}

function newchallanadvance() {
    adv = parseFloat($('input.newchallan-advanceprice').val())
    value = parseFloat($('input.newchallan-totalprice').val().replace("₹", "").trim())
    if (adv) {
        value -= adv;
    }
    net = `₹ ${value}.00`
    $("input.newchallan-netprice").val(net);
}

function newchallanamount() {
    var sum = 0;
    value = `₹ 0.00`;
    $('input.form-control.newchallan-amount').each(function() {
        if (this.value) {
            sum += parseFloat(this.value);
            value = `₹ ${sum}.00`;
        }
    });
    $("input.newchallan-totalprice").val(value);
    newchallanadvance();
}

function raqchange1(part_id) {
    var rate = $('input.rate' + part_id).val();
    console.log("rate", rate);
    var qty = $('input.qty' + part_id).val();
    console.log("qty", qty);
    var amt = parseFloat(rate * qty)
    console.log("amt", amt);
    $("input.amount.part" + part_id).val(amt);
    newchallanamount(part_id, );
}
// add new line
$(document).ready(function() {

    var max_fields = 15;

    var newchallan_wraps = $(".newchallan_input_fields_wrap");
    var newchallan_add_button = $(".newchallan_add_field_button");
    var x = 1;
    $(newchallan_add_button).click(function(e) {
        e.preventDefault();
        if (x < max_fields) {
            x++;
            $(newchallan_wraps).append('<div class="row"><div class ="col-md-3 col-sm-12"><div class= "form-group"><label>Particulars</label><input type="text" class="form-control" id="nc-particulars-desc"></div></div><div class="col-md-2 col-sm-12"><div class= "form-group"><label>Size</label><input type="text" class="form-control" id="nc-size-desc"></div></div><div class="col-md-2 col-sm-12"><div class ="form-group"><label>Qty</label><input type="number" class="form-control qty' + x + '" onchange=raqchange1(' + x + ')  id="uc-qty-desc" value="0"></div></div ><div class="col-md-2 col-sm-12"><div class ="form-group"><label>Rate</label><input type="number" class="form-control rate' + x + '" onchange=raqchange1(' + x + ')  id="uc-rate-desc" value="0"></div></div ><div class="col-md-2 col-sm-12"><div class ="form-group"><label>Amount</label><input type="number" class="form-control newchallan-amount' + x + '" onchange=newchallanamount() id="nc-amount-desc" disabled></div></div ><div class="col-md-1 col-sm-12"><div style="cursor:pointer;background-color:red;" class="newchallan_remove_field btn btn-info">X</div></div></div>');
            //add input box
        }
    });
    $(newchallan_wraps).on("click", ".newchallan_remove_field", function(e) {
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        let asum = 0
        value = `₹ 0.00`;
        $('input.form-control.newchallan-amount').each(function() {
            value = `₹ 0.00`;
            if (this.value) {
                asum += parseFloat(this.value);
                value = `₹ ${asum}.00`;
            }
        });
        x--;
        $("input.newchallan-totalprice").val(value);
        newchallanadvance();
    })
});



// print page
function printDiv(divName) {
    var printContents = document.getElementById(divName).innerHTML;
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
    location.reload(true)
}

function getdata(id) {
    const formData = {}
    const desc = {}
    $('#' + id + ' input, #' + id + ' select').each(
        function(index) {
            var input = $(this);
            try {
                if (input.attr('id').includes("price")) {
                    formData[input.attr('id')] = parseFloat(input.val().replace("₹", "").trim())
                } else if (input.attr('id').includes("desc")) {
                    if (input.attr('id') in formData) {
                        formData[input.attr('id')] = formData[input.attr('id')] + " " + input.val()
                    } else {
                        formData[input.attr('id')] = input.val()
                            // formData[input.attr('id')] = []
                            // formData[input.attr('id')].push(input.val())
                    }
                } else {
                    formData[input.attr('id')] = input.val()
                }
            } catch (err) {
                // ...arguments
            }
            // console.log(desc)

        }
    );
    return formData;
}

function savechallan(formData, id) {
    if (id) {
        url = '/updatechallan/' + id + '/'
    } else {
        url = '/addnewchallan/'
    }
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        success: function(response) {
            $('#new-challan').modal('hide');
            $('#edit-challan' + response.challan).modal('hide');
            if (response.response == 'added') {
                var paragraph = document.getElementById("body-text");
                paragraph.textContent = "Challan No " + response.challan + " Saved";
            } else {
                var paragraph = document.getElementById("body-text");
                paragraph.textContent = "Challan No MG" + response.challan + " Updated";
            }
            $('#success-modal').modal('show');
        },
        error: function(response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    });
}


$(document).ready(function() {
    n = new Date();
    y = n.getFullYear();
    m = n.getMonth() + 1;
    d = n.getDate();
    try {
        document.getElementById("due-date").innerHTML = d + "/" + m + "/" + y;
    } catch (error) {

    }
    $('#addnewchallan').on('submit', function(e) {
        e.preventDefault();
        var formData = getdata("addnewchallan")
        var challan_id = 0
        savechallan(formData, challan_id);
    });
    $("form").submit(function(e) {
        e.preventDefault();
        // Get the submit button element
        try {
            var updateid = $(document.activeElement).attr('data');
            if (updateid.includes("updatechallan")) {
                var formData = getdata(updateid)
                var challan_id = updateid.replace('updatechallan', '')
                savechallan(formData, challan_id);
            }
        } catch (error) {

        }
    });
    $('.confirmation-btn').on('click', function(e) {
        e.preventDefault();
        var Id = this.id;
        var _id = Id.replace('deletechallan', '')
        if (Id.includes("deletechallan")) {
            $.ajax({
                url: '/deletechallan/' + _id + '/',
                type: 'POST',
                success: function(response) {
                    $('#new-challan').modal('hide');
                    var paragraph = document.getElementById("body-text");
                    paragraph.textContent = "Challan No " + response.challan + " Deleted";

                    $('#success-modal').modal('show');
                },
                error: function(response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            });
        }
    });
    $('.cust-noexist').hide();
    $('#cust-exist').hide();
    $('#myproducts').hide();
    $('#myproducts1').hide();
    $('#myproducts2').hide();
    $('#np-custcode').val('')
    $('#np-custname').val('')
    $('#creds').hide()
});

function reloadpage() {
    window.location.reload();
}

function raqchange(part_id, challan_id) {
    var rate = $('input.rate' + part_id).val();
    console.log("rate", rate);
    var qty = $('input.qty' + part_id).val();
    console.log("qty", qty);
    var amt = parseFloat(rate * qty)
    console.log("amt", amt);
    $("input.amount.part" + part_id).val(amt);
    amountchange(part_id, challan_id);
}

const mySelect = document.getElementById("textSelect");
const inputOther = document.getElementById("form12");
const labelInput = document.getElementById("inputLabel");
const divInput = document.getElementById("inputDiv");
const selectDiv = document.getElementById("textSelectdiv");

// mySelect.addEventListener('optionSelect.mdb.select', function(e) {
//     const SelectValue = document.getElementById('textSelect').value;
//     if (SelectValue === 'customOption') {
//         inputOther.style.display = 'inline';
//         inputOther.removeAttribute('disabled');
//         labelInput.classList.remove('disaplayInput');
//         divInput.classList.remove('disaplayInput');
//         selectDiv.style.display = 'none';
//         inputOther.focus();
//         mySelect.disabled = 'true';

//     } else {
//         a.style.display = 'none';
//     }
// })

function hideInput() {
    if (inputOther !== null && inputOther.value === "") {
        inputOther.style.display = 'none';
        inputOther.setAttribute('disabled', '');
        selectDiv.style.display = 'inline';
        mySelect.removeAttribute('disabled');
        labelInput.classList.add('disaplayInput');
        divInput.classList.add('disaplayInput');
    }
}

function productratechng() {
    var rate = $('#np-custrate').val();
    console.log("rate", rate);
    var qty = $('#np-custqty').val();
    console.log("qty", qty);
    var amt = parseFloat(rate * qty)
    console.log("amt", amt);
    $('#np-custamount').val(amt);
}

function custratechng(code) {
    var rate = $('#ft-custrate' + code).val();
    console.log("rate", rate);
    var qty = $('#ft-custqty' + code).val();
    console.log("qty", qty);
    var amt = parseFloat(rate * qty)
    console.log("amt", amt);
    $('#ft-custamount' + code).val(amt);
}

function custjobchange(code) {
    var jobname = $('#ft-custjobname' + code).val();
    console.log("jobname", jobname);
    if (jobname == "flyers") {
        document.getElementById("ft-custprcolor" + code).disabled = true;
        document.getElementById("ft-custpcolor" + code).disabled = true;
    } else if (jobname == "pamphlet") {
        document.getElementById("ft-custprcolor" + code).disabled = false;
        document.getElementById("ft-custpcolor" + code).disabled = false;
        document.getElementById("size4").style.display = "none";
        document.getElementById("size9").style.display = "none";
    } else {
        document.getElementById("ft-custprcolor" + code).disabled = false;
        document.getElementById("ft-custpcolor" + code).disabled = false;
        document.getElementById("size4").style.display = "flex";
        document.getElementById("size9").style.display = "flex";
    }
}

function jobchange() {
    var jobname = $('#np-jobname').val();
    console.log("jobname", jobname);
    if (jobname == "flyers") {
        document.getElementById("np-prcolor").disabled = true;
        document.getElementById("np-pcolor").disabled = true;
    } else if (jobname == "pamphlet") {
        document.getElementById("np-prcolor").disabled = false;
        document.getElementById("np-pcolor").disabled = false;
        document.getElementById("size4").style.display = "none";
        document.getElementById("size9").style.display = "none";
    } else {
        document.getElementById("np-prcolor").disabled = false;
        document.getElementById("np-pcolor").disabled = false;
        document.getElementById("size4").style.display = "flex";
        document.getElementById("size9").style.display = "flex";
    }
}

function addnewproduct() {
    $("#myproducts").clone().appendTo(".newchallan_input_fields_wrap");
}

function savedetails() {
    var formData = getdata("addnewcustomer")
    $.ajax({
        url: '/customer/',
        type: 'POST',
        data: formData,
        success: function(response) {
            $("#new-customer .close").click();
            if (response.response == 'added') {
                var paragraph = document.getElementById("body-text");
                paragraph.textContent = "Customer Saved";
            } else {
                var paragraph = document.getElementById("body-text");
                paragraph.textContent = "Customer Updated";
            }
            $('#np-custcode').val(response.customercode)
            $('#np-custname').val(response.customername)
            $('#new-product').modal('show')
            $('#myproducts').show();
            $('#myproducts1').show();
            $('#myproducts2').show();
            console.log("success");
        },
        error: function(response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    });
}

function custchange() {
    custcode = $('#np-custcode').val();
    $.ajax({
        url: '/customer/',
        type: 'POST',
        data: { 'custcode': custcode },
        success: function(response) {
            if (response.cust_name == 'not-exist') {
                $('#cust-exist').hide();
                $('#myproducts').hide();
                $('#myproducts1').hide();
                $('#myproducts2').hide();
                $('.cust-noexist').show();
                $('#np-custname').val('');
            } else {
                $('.cust-noexist').hide();
                $('#cust-exist').show();
                $('#np-custname').val(response.cust_name);
                $('#myproducts').show();
                $('#myproducts1').show();
                $('#myproducts2').show();
            }
        },
        error: function(response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    });
}

$(document).ready(function() {
    $('#addnewprod').on('submit', function(e) {
        e.preventDefault();
        var formData = getdata("addnewprod")
        checkreq(formData);
    });
    $('#addnewmember').on('submit', function(e) {
        e.preventDefault();
        var formData = getdata("addnewmember")
        $.ajax({
            url: '/teams/',
            type: 'POST',
            data: formData,
            success: function(response) {
                $("#new-member .close").click();
                if (response.response == 'added') {
                    var paragraph = document.getElementById("body-text");
                    paragraph.textContent = "Member Added";
                } else {
                    var paragraph = document.getElementById("body-text");
                    paragraph.textContent = "Member Updated";
                }
                $('#success-modal').modal('show');
            },
            error: function(response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        });
    });
    // $('#loginuser').on('submit', function(e) {
    //     e.preventDefault();
    //     var loginData = getdata("loginuser")
    //     $.ajax({
    //         url: '/login/',
    //         type: 'POST',
    //         data: loginData,
    //         success: function(response) {
    //             if (response.memberlogin.member_des == 'MD') {
    //                 $.ajax({
    //                     url: '/dash/',
    //                     type: 'POST',
    //                     data: loginData,
    //                     success: function(response) {
    //                         if (response.memberlogin.member_des == 'MD') {
    //                             var domain = window.location.origin;
    //                             setInterval(function() {
    //                                 window.location.replace(domain + '/dash');
    //                             }, 3000);
    //                             console.log("hii replace window")
    //                         } else if (response.memberlogin.member_des == 'Designer') {
    //                             var domain = window.location.origin;
    //                             window.location.replace(domain + '/product');
    //                         } else {
    //                             $('#creds').show()
    //                         }
    //                     },
    //                     error: function(response) {
    //                         // alert the error if any error occured
    //                         alert(response["responseJSON"]["error"]);
    //                     }
    //                 });
    //             } else if (response.memberlogin.member_des == 'Designer') {
    //                 var domain = window.location.origin;
    //                 window.location.replace(domain + '/product');
    //             } else {
    //                 $('#creds').show()
    //             }
    //         },
    //         error: function(response) {
    //             // alert the error if any error occured
    //             alert(response["responseJSON"]["error"]);
    //         }
    //     });
    // });

});

function isNumberKey(evt) {
    var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57) && length(charCode) == 10)
        return false;
    return true;
}

function checkreq(formData) {
    if (formData["np-custjobname"] == "Choose..." || formData["np-custsize"] == "Choose..." || formData["np-custpside"] == "Choose..." || formData["np-custprcolor"] == "Choose..." || formData["np-custpname"] == "Choose..." || formData["np-custpgsm"] == "Choose..." || formData["np-custpcolor"] == "Choose..." || formData["np-custlamination"] == "Choose..." || formData["np-custfolding"] == "Choose..." || formData["np-custperforated"] == "Choose..." || formData["np-custqty"] == "Choose..." || formData["np-custrate"] == "Choose...") {
        alert("Please fill all the field");
    } else {
        $.ajax({
            url: '/product/',
            type: 'POST',
            data: formData,
            success: function(response) {
                $("#new-product .close").click();
                if (response.response == 'added') {
                    var paragraph = document.getElementById("body-text");
                    paragraph.textContent = "Product Saved";
                } else {
                    var paragraph = document.getElementById("body-text");
                    paragraph.textContent = "Product Updated";
                }
                $('#success-modal').modal('show');
            },
            error: function(response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        });
    }
}

function savejobcust(code) {
    var formData = getdata("oldcustprod" + code)
    try {
        formData.set("code", code)
    } catch {
        formData.code = code
    }
    $.ajax({
        url: '/savecustomer/',
        type: 'POST',
        data: formData,
        success: function(response) {
            $("#jobthroughcut" + code + " .close").click();
            if (response.response == 'added') {
                var paragraph = document.getElementById("body-text");
                paragraph.textContent = "Product Saved";
            } else {
                var paragraph = document.getElementById("body-text");
                paragraph.textContent = "Product Updated";
            }
            $('#success-modal').modal('show');
        },
        error: function(response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    });
}