$(document).ready(function() {
    setSearchAutocomplete();
})


var baseAddress = ["localhost://"]

var nbaTeams = [
{name: "Does Customer Gender affect Sales?" , link: "v=gender-sales", thumb: "https://f001.backblaze.com/file/thumbspublic212/sales.jpg", source: "Sales Data", description: "Sales breakdown by Gender", status: "NEW", popularity: "128"},
{name: "Does the Customer's Residence State affect Sales?" , link: "v=cstate-sales", thumb: "https://f001.backblaze.com/file/thumbspublic212/sales.jpg", source: "Sales Data", description: "Sales breakdown by Customer State", status: "NEW", popularity: "369"},
{name: "Which Product Category has the Highest Sales?" , link: "v=cat-sales", thumb: "https://f001.backblaze.com/file/thumbspublic212/sales.jpg", source: "Sales Data", description: "Sales breakdown by Category", status: "NEW", popularity: "436"},
{name: "How Does Customer Type affect Sales?" , link: "v=nvo-sales", thumb: "https://f001.backblaze.com/file/thumbspublic212/sales.jpg", source: "Sales Data", description: "Sales breakdown by Customer Type", status: "URGENT", popularity: "451"},
{name: "How does Credit / Cash / Denying Refunds affect Future Buying?" , link: "v=cb-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Customer Behaviour Post Refund Request", status: "URGENT", popularity: "119"},
{name: "How does Refund Type affect Future Customer Spend?" , link: "v=cs-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Customer Spend Post Refund", status: "URGENT", popularity: "316"},
{name: "Is there a Difference between Full & Partial Refunds?" , link: "v=partialfull-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by partial/full/denied ", status: "URGENT", popularity: "179"},
{name: "Which Product Category has the highest refunds?" , link: "v=cat-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by Product Category", status: "URGENT", popularity: "477"},
{name: "Does the Refund Request Reason affect Refund Behaviour?" , link: "v=reason-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by Refund Reason", status: "URGENT", popularity: "210"},
{name: "Does Gender matter when it comes to Refunds and Future Behaviour?" , link: "v=gender-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by Gender", status: "", popularity: "418"},
{name: "Does the Refund Amount affect Future Customer Behaviour?" , link: "v=amount-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by Amount", status: "", popularity: "217"},
{name: "Do First Time Buyers React the same to Refunds for Future Behaviour?" , link: "v=previous-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by Previous Purchase Qty", status: "", popularity: "240"},
{name: "How Many Post-Refund Customers are Still Active?" , link: "v=active-refunds", thumb: "https://f001.backblaze.com/file/thumbspublic212/refunds.jpg", source: "Refund Data", description: "Refunds by Customer Currently Active?", status: "", popularity: "408"},
{name: "John Doe johndoe@bigpond.com" , link: "c=johndoe@bigpond.com", thumb: "https://f001.backblaze.com/file/thumbspublic212/customers2.png", source: "Customer Profile", description: "John Doe Customer Behaviour Drilldown", status: "Customer", popularity: "414"},
{name: "Jane Smith janesmith@bigpond.com" , link: "c=janesmith@bigpond.com", thumb: "https://f001.backblaze.com/file/thumbspublic212/customers2.png", source: "Customer Profile", description: "Jane Smith Customer Behaviour Drilldown", status: "Customer", popularity: "458"},
{name: "Who Are My Top Customers?" , link: "dtop", thumb: "https://f001.backblaze.com/file/thumbspublic212/dashtest.png", source: "Automatic Report", description: "Automatically Generated Top Customer Dashboard", status: "DASHBOARD", popularity: "211"}
];



function setSearchAutocomplete() {
    var searchlist = new Bloodhound({
        datumTokenizer: function(d) {return Bloodhound.tokenizers.whitespace(d.name); },
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: nbaTeams
    });
    // .typeahead is the selector for my search bar
    setTypeaheadBinding('.typeahead', searchlist);
}

function setTypeaheadBinding(selector, adapter) {
    $(selector).typeahead(null, {
        name: 'searchlist',
        displayKey: 'name',
        source: adapter.ttAdapter(),
        templates: {
            empty: [
                '<div class="empty-message text-center">',
                'No Answers Found<br>',
                '<a href="../ask" class="text-center">Ask Us Directly</a>',
                '</div>',
            ].join('\n'),
            suggestion: function(data) {
                return ['<div class="searchbox-card">',
                      '<img class="searchbox-card-poster" src="' + data.thumb + '">',
                      '<div class="searchbox-card-details">',
                      '<div class="searchbox-card-name">' + data.name + '</div>',
                      '<div class="searchbox-card-year pull-right">' + data.status + '</div>',
                      '<div class="searchbox-card-plot">' + data.description + '</div>',
                      '</div>',
                      '</div>'].join('\n');
            },
            footer: '<a href="../ask" id="view-more-searchlist" class="btn btn-primary btn-sm text-center center-block">View More</a>'
        }
    });
}

$('.typeahead').on('typeahead:selected typeahead:autocompleted', function(e, datum) {
    window.location.href = datum.link;
});