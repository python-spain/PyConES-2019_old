<template>
    <div class="container footer">
        <div class="row">
            <div class="col-sm-10 offset-sm-1 col-md-3">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-12">
                            {{ $t("footer.follow") }}
                        </div>
                        <div class="col-sm-12 icons">
                            <a href="https://www.es.python.org/">
                                <font-awesome-icon icon="heart" />
                            </a>
                            <a href="https://twitter.com/pycones?lang=en">
                                <font-awesome-icon :icon="['fab', 'twitter']" />
                            </a>
                            <a href="https://github.com/python-spain">
                                <font-awesome-icon :icon="['fab', 'github']" />
                            </a>
                        </div>
                        <div class="col-sm-12">
                            {{ $t("footer.touch")  }}
                        </div>
                        <div class="col-sm-12 icons">
                            <a href="mailto:contact@2019.es.pycon.org">
                                <font-awesome-icon icon="envelope" />
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-10 offset-sm-1 col-md-7 offset-md-0 newsletter">
                {{ $t("footer.subscribe") }}
                <div class="container newsletter-form">
                    <div class="row">
                        <div class="offset-sm-1 col-sm-10 offset-lg-3 col-lg-6">
                            <form action="https://twitter.us16.list-manage.com/subscribe/post?u=b340cff322b1d7f8a81ceab94&id=53e88e395a">
                                <input type="hidden" name="u" value="b340cff322b1d7f8a81ceab94"/>
                                <input type="hidden" name="id" value="53e88e395a"/>
                                 <b-input-group>
                                    <b-form-input name="EMAIL" :placeholder="$t('footer.mail')" type="email"></b-form-input>
                                    <b-input-group-append>
                                      <b-button type="submit">{{ $t("footer.submit")  }}</b-button>
                                    </b-input-group-append>
                                  </b-input-group>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    name: "Footer",
    data: () => ({
      icons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-instagram'
      ]
    }),
    methods: {
        subscribe: () =>{
            console.log("Hola mundo")
        }
    },
  }
</script>
