<template>
  <v-combobox
    id="combobox"
    v-model="model"
    :filter="filter"
    :hide-no-data="!search"
    :items="items"
    :search-input.sync="search"
    hide-selected
    label="Add Your Tag"
    multiple
    small-chips
    solo
    flat
  >
    <template v-slot:no-data>
      <v-list-tile>
        <span class="subheading">Create</span>
        <v-chip
          :color="`${colors[((nonce - 1)%6)]} lighten-3`"
          label
          small
        >
          {{ search }}
        </v-chip>
      </v-list-tile>
    </template>
    <template v-slot:selection="{ item, parent, selected }">
      <v-chip
        v-if="item === Object(item)"
        :color="`${item.color} lighten-3`"
        :selected="selected"
        label
        small
      >
        <span class="pr-2">
          {{ item.text }}
        </span>
        <v-icon
          small
          @click="parent.selectItem(item)"
        >close</v-icon>
      </v-chip>
    </template>
    <template v-slot:item="{ index, item }">
      <v-list-tile-content>
        <v-text-field
          v-if="editing === item"
          v-model="editing.text"
          autofocus
          flat
          background-color="transparent"
          hide-details
          solo
          @keyup.enter="edit(index, item)"
        ></v-text-field>
        <v-chip
          v-else
          :color="`${item.color} lighten-3`"
          dark
          label
          small
        >
          {{ item.text }}
        </v-chip>
      </v-list-tile-content>
      <!-- <v-spacer></v-spacer> -->
      <v-list-tile-action @click.stop>
        <v-btn
          icon
          @click.stop.prevent="edit(index, item)"
        >
          <v-icon>{{ editing !== item ? 'edit' : 'check' }}</v-icon>
        </v-btn>
      </v-list-tile-action>
    </template>
  </v-combobox>
</template>

<script>
  export default {
    data: () => ({
      activator: null,
      attach: null,
      colors: ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'],
      editing: null,
      index: -1,
      items: [
        { header: 'Select an option or create one' }
      ],
      nonce: 1,
      menu: false,
      model: [

      ],
      x: 0,
      search: null,
      y: 0
    }),
    watch: {
      model (val, prev) {
        if (val.length === prev.length) return
        this.model = val.map(v => {
          if (typeof v === 'string') {
            this.nonce = this.model.length + 1
            v = {
              text: v,
              color: this.colors[((this.nonce - 1)%6)]
            }

            this.items.push(v)
            this.nonce++
          }

          return v
        })
      }
    },
    methods: {
      getTags(){
        return this.model;
      },
      getTagsForDb(){
        var tags = [];

        for(var i = 0; i < this.model.length; i++){
          tags.push(this.model[i].text);
        }

        return tags;
      },
      edit (index, item) {
        if (!this.editing) {
          this.editing = item
          this.index = index
        } else {
          this.editing = null
          this.index = -1
        }
      },
      filter (item, queryText, itemText) {
        if (item.header) return false
        const hasValue = val => val != null ? val : ''
        const text = hasValue(itemText)
        const query = hasValue(queryText)
        return text.toString()
          .toLowerCase()
          .indexOf(query.toString().toLowerCase()) > -1
      },

      setTags(tags){
        if(tags != null){
          for(var i in tags){
            this.model.push(tags[i]);
          }
          this.nonce = tags.length + 1

          console.log(this.colors);
        }
      }
    }
  }
</script>

<style media="screen" scoped>
  #hashtag > div > div >.v-input__slot{
    border: 1px solid #ddd;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
  }
</style>
