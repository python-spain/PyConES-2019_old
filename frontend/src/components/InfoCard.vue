<template>
    <b-card :title="title" :img-src="image_src" img-alt="Su cara" img-top>
        <b-card-text>{{description}}</b-card-text>
        <b-button v-if="button_text" :href=this.link variant="primary">{{button_text}}</b-button>
    </b-card>   
</template>

<script>

export default {
    name: "InfoCard",
    props: ['title', 'image_src', 'description', 'link', 'button_text'],
    //data() {
    //    return {
    //        "data": {
    //            "keynoters": [
    //                {
    //                    "title": "Safia Abdalla",
    //                    "image": "static/keynoters/safia.jpg",
    //                    "description": "Safia is an open source developer, writer, and a software engineer at Microsoft. She is passionate about bringing people together to build great things.",
    //                    "link": ""
    //                },
    //                {
    //                    "title": "Francisco Javier Ordoñez",
    //                    "image": "static/keynoters/fj.jpg",
    //                    "description": "Lead Data Scientist en StyleSage. Es un profesional multidisciplinar con más de 11 años de experiencia en el área de inteligencia artificial, habiendo trabajado de investigador, ingeniero, profesor y consultor.",
    //                    "link": ""
    //                },
    //                {
    //                
    //                    "title": "Comming soon",
    //                    "image": "",
    //                    "description": "Comming soon",
    //                    "link": ""
    //                }
    //            ],
    //            "information": [
    //                {
    //                    "title": "The event",
    //                    "description": "PyConES es la conferencia de la comunidad Python española. PyConES se celebrará por séptima vez del 04 al 06 de octubre de 2019 en Alicante, tras seis exitosas ediciones en Madrid, Zaragoza, Valencia, Almería, Cáceres y Málaga, siguiendo el formato del evento mundial de PyCon.",
    //                    "image": "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    //                    "link": ""
    //                },
    //                {
    //                    "title": "Tickets",
    //                    "description": "The tickets will be soon available. Until then you can follow us on twitter to get the last news.",
    //                    "image": "https://burnzozobra.com/wp-content/uploads/2016/05/event-tickets-pic71_0.png",
    //                    "link": "#"
    //                },
    //                {
    //                    "title": "Call for Papers!",
    //                    "description": "Our call for papers is now open, follow the link to propose a talk",
    //                    "image": "https://csrbox.org/news/1550140963call%20for%20papers.jpg",
    //                    "link": "https://easychair.org/cfp/pycones2019"
    //                }
    //            ]
    //        }
    //    }
    //},
    //created (){
    //    let instance_data = this.data[this.source][this.id]

    //    this.title = instance_data.title;
    //    this.image_src = instance_data.image;
    //    this.description = instance_data.description;
    //    this.link = instance_data.link;
    //} 
}
</script>
