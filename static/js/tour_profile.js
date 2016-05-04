var tour = new Shepherd.Tour({
                  defaults: {
                    classes: 'shepherd-theme-square-dark',
                    // scrollTo: true
                  }
                });

                tour.addStep('myStep1', {
                  title: 'Please give us your full name',
                  text: 'So we know who you are',
                  showCancelLink: true,
                  attachTo: '#div_id_customer_name right',
                  buttons: [
                    {
                      text: 'Skip Tour',
                      classes: 'shepherd-button-secondary',
                      action: function() {
                        return tour.hide();
                      }},
                      {
                      text: 'Next Step',
                      classes: 'shepherd-button-primary',
                      action: function() {
                        return tour.next();
                      }}
                  ]
                });

                tour.addStep('myStep2', {
                  title: 'And your website',
                  text: 'The domain your shop is hosted at (should start with WWW)',
                  attachTo: '#div_id_company_website right',
                  buttons: [
                    {
                      text: 'Skip Tour',
                      classes: 'shepherd-button-secondary',
                      action: function() {
                        return tour.hide();
                      }},
                      {
                      text: 'Next Step',
                      classes: 'shepherd-button-primary',
                      action: function() {
                        return tour.next();
                      }}
                  ]
                });

                tour.addStep('myStep3', {
                  title: 'Then your company name',
                  text: 'Only if you have one, otherwise just type NA',
                  attachTo: '#div_id_company_name right',
                  buttons: [
                    {
                      text: 'Skip Tour',
                      classes: 'shepherd-button-secondary',
                      action: function() {
                        return tour.hide();
                      }},
                      {
                      text: 'Next Step',
                      classes: 'shepherd-button-primary',
                      action: function() {
                        return tour.next();
                      }}
                  ]
                });

                tour.addStep('myStep4', {
                  title: 'The Country of our company',
                  text: 'So we know where in the world you are',
                  attachTo: '#div_id_company_country right',
                  buttons: [
                    {
                      text: 'Skip Tour',
                      classes: 'shepherd-button-secondary',
                      action: function() {
                        return tour.hide();
                      }},
                      {
                      text: 'Next Step',
                      classes: 'shepherd-button-primary',
                      action: function() {
                        return tour.next();
                      }}
                  ]
                });

                tour.addStep('myStep5', {
                  title: 'Last and least, your billing currency',
                  text: 'The currency you do your company accounting in (eg: USD, AUD, CAD, EUR)',
                  attachTo: '#div_id_company_primary_currency right',
                  buttons: [
                    {
                      text: 'Skip Tour',
                      classes: 'shepherd-button-secondary',
                      action: function() {
                        return tour.hide();
                      }},
                      {
                      text: 'Next Step',
                      classes: 'shepherd-button-primary',
                      action: function() {
                        return tour.next();
                      }}
                  ]
                });

                tour.addStep('myStep6', {
                  title: 'GREAT. ALL DONE',
                  text: 'Now click SAVE to continue',
                  attachTo: '#savebutton top',
                  buttons: [
                    {
                      text: 'Done',
                      classes: 'shepherd-button-primary',
                      action: function() {
                        return tour.hide();
                      }}
                  ]
                });

            tour.start()