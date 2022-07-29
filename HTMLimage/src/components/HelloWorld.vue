<template>
<v-container class="gap-20 d-flex flex-column">
  <div class="d-flex flex-column gap-20">
       <v-slider
          v-model="width"
          hide-details
          :max='2560'
          :min="100"
          :step="1"
          thumb-label
          color="primary"
        >
        <template v-slot:append>
          <v-text-field
            v-model="width"
            hide-details
            label="Width"
            color="primary"
            variant="outlined"
            style="width: 150px "
          ></v-text-field>
        </template>
      </v-slider>
        <v-slider
          v-model="height"
          hide-details
          :max="1080"
          :min="100"
          :step="1"
          thumb-label
          color="primary"
        >
        <template v-slot:append>
          <v-text-field
            v-model="height"
            hide-details
            label="Height"
            color="primary"
            variant="outlined"
            style="width: 150px "
          ></v-text-field>
        </template>
      </v-slider>
        <v-textarea
        v-model="text"
        hide-details
        auto-grow
        filled
        color="deep-purple"
        label="Text"
        rows="1"
      ></v-textarea>
      <div class="d-flex gap-20">
        <div class="d-flex flex-column gap-20">
          <h2>Создать без запроса</h2>
          <v-select
          hide-details
          varian="outlined"
          label="Format"
          :items="['jpeg', 'png', 'svg']"
          v-model="format1"
          color="primary"
          > </v-select>
          <div class="d-flex justify-center">
            <v-btn @click="convertDomToImg" color="primary">Создать</v-btn>
          </div>
          <div class="result align-center flex-column d-flex gap-20">
            <h2>Result img</h2>
            <img :src="imgSrc1" alt="">
          </div>
        </div>
        <div class="d-flex flex-column gap-20">
          <h2>Получить через сервис</h2>
          <v-select
          hide-details
          varian="outlined"
          label="Format"
          color="primary"
          :items="['jpg', 'png', 'webp']"
          v-model="format2" 
          > </v-select>
          <div class="d-flex justify-center">
            <v-btn @click="convertRequest" color="primary">Отправить запрос</v-btn>
          </div>
          <div class="result align-center flex-column d-flex gap-20">
            <h2>Result img</h2>
            <img :src="imgSrc2" alt="">

          </div>
        </div>
      </div>
    </div>

    <h2>Preview</h2>
    <div class="preview"
      ref="preview"
         :style="{'width': `${width}px`, 'height': `${height}px`}"
      style="display:flex;
             justify-content: center;
             align-items: center;
             text-align: center;
             color: #6200EE;
             padding: 10px;
             border: 3px solid #6200EE;"
      >
      {{ text }}
    </div>
</v-container>
</template>

<script>
import domtoimage from 'dom-to-image';
import axios from "axios";

export default {
  name: 'HelloWorld',
  data() {
    return {
      width: 100,
      height: 100,
      text: 'Lorem',
      imgSrc1: null,
      imgSrc2: null,
      format1: 'png',
      format2: 'png',
    }
  },
  methods: {
    convertDomToImg() {
      switch(this.format1) {
        case 'jpeg':
          domtoimage.toJpeg(this.$refs.preview, {bgcolor: '#fff'}).then((dataUrl) => {
            this.imgSrc1 = dataUrl
          })
          break;
        case 'png':
          domtoimage.toPng(this.$refs.preview).then((dataUrl) => {
            this.imgSrc1 = dataUrl
          })
          break;
        case 'svg':
          domtoimage.toSvg(this.$refs.preview).then((dataUrl) => {
            this.imgSrc1 = dataUrl
          })
          break;

      }
    },
    async convertRequest() {
      const payload = {
        html: this.$refs.preview.outerHTML,
      }
      const { API_ID, API_KEY } = {API_ID: '790276b7-0a75-4315-a803-7b925f9d89fc', API_KEY: 'd7867654-d7a4-43a8-a449-5d75e63ae719'}

      console.log(API_ID, API_KEY)

      const queryParams = `?width=${this.width}&height=${this.height}`

      const response = await axios.post(`https://hcti.io/v1/image/`,
          payload, {
          auth: {
            username: API_ID,
            password: API_KEY
          }
      })
      this.imgSrc2 = response.data.url + `.${this.format2}/${queryParams}`
      console.log(response)
    }
  },
}
</script>

<style>
.v-container {
  max-width: 100% !important;
  margin: 0 !important;
}
.gap-20 {
  gap: 20px;
}
.v-btn{
  width: 200px ;
}
.result {
  color: rgb(var(--v-theme-primary));
}
</style>
