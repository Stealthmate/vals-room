<template>
  <v-container>
    <v-card v-for="item, i in theDrinks" :key="i" class="my-5">
      <v-img :src="require(`@/assets/${item.img}`)" contain width="100vw"></v-img>
      <div class="d-flex flex-grow-1 align-stretch flex-column">
        <v-card-title>{{ item.name }}</v-card-title>
        <v-card-subtitle class="d-flex flex-row"> {{ item.reading }} <v-spacer /> {{item.abv}}%</v-card-subtitle>
        <v-card-text class='text--primary'>{{ item.description }}</v-card-text>
      </div>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: 'TheBottlesPage',
    computed: {
      theDrinks() {
        return [
          {
            name: 'Ocean Water',
            reading: 'オーシャン・ウォーター',
            description: '海をイメージした色でオレンジの味とココナッツの香りを活かしたとても爽やかな飲み物．',
            abv: 14,
            img: 'ocean-water.jpg'
          },
          {
            name: 'Midori June Bug',
            reading: 'ミドリ・ジューン・バグ',
            description: 'メロンリキュールをベースにパイナップル，バナナ，ココナッツのお味と組み合わせ，おしゃれな飾りで鮮やかな色に仕上げたカクテル．フルーツ好きな人にぴったり！',
            abv: 14,
            img: 'midori-june-bug.jpg'
          },
          {
            name: 'Tequila Sunrise',
            reading: 'テキーラサンライズ',
            description: 'asd',
            abv: 12,
            img: 'tequila-sunrise.jpg'
          },
          {
            name: 'Blue Lagoon',
            reading: 'ブルーラグーン',
            description: 'asd',
            abv: 14,
            img: 'blue-lagoon.jpg'
          },
          // { 
          //   name: 'Piña Colada',
          //   reading: 'ピニャコラーダ',
          //   description: 'パイナップルジュースと牛乳にココナッツの味を加えたプエルトリコ発祥のカクテル',
          //   abv: 8,
          //   original: false,
          //   img: 'ocean-water.jpg'
          // },
          // { 
          //   name: 'Piñana Colada',
          //   reading: 'ピニャナコラーダ',
          //   description: 'ピニャコラーダにバナナの味を加えたトロピカル風のカクテル',
          //   abv: 4,
          //   original: true,
          //   img: 'ocean-water.jpg'
          // },
          // {
          //   name: 'Malibu Surf',
          //   reading: 'マリブサーフ',
          //   description: 'オレンジの味がする青色のリキュールにトニックウォータを加えた爽やかなドリンク',
          //   abv: 10,
          //   img: 'ocean-water.jpg'
          // },
          // {
          //   name: 'Campari Negroni',
          //   reading: 'カンパリネグローニ',
          //   description: 'オレンジの味がする青色のリキュールにトニックウォータを加えた爽やかなドリンク',
          //   abv: 26,
          //   img: 'ocean-water.jpg'
          // },
          // {
          //   name: 'Martini',
          //   reading: 'マティーニ',
          //   description: '青色リキュールにトニックウォータを加えた爽やかなドリンク',
          //   abv: 36,
          //   img: 'ocean-water.jpg'
          // },
          // {
          //   name: 'Ikiri',
          //   reading: 'イキリ酒',
          //   description: 'asd',
          //   abv: 26,
          //   img: 'ocean-water.jpg'
          // },
          // {
          //   name: 'Sauza Paloma',
          //   reading: 'クリームオブココナッツ',
          //   description: 'asd',
          //   abv: 30,
          //   img: 'ocean-water.jpg'
          // }
        ]
      }
    }
  }
</script>

<style scoped>

  ruby:nth-child(n+2)::before {
    content: "\00a0";
  }
</style>
