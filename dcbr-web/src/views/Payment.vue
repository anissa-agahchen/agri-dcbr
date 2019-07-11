<template>
  <v-container>
    <v-tabs color="blue darken-4" dark slider-color="blue lighten-2">
      <v-tab ripple>Credit Card</v-tab>
      <v-tab ripple>Cheque</v-tab>
      <v-tab ripple>Cash</v-tab>
      <v-tab-item>
        <v-card>
          <v-card-text>
            <v-text-field v-model="mask" label="Name on the card"></v-text-field>
          </v-card-text>
          <v-card-text>
            <v-text-field v-model="value" :mask="mask" label="Credit card number"></v-text-field>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <h4>Mailing Address</h4>
            <p>
              Provincial Sales Tax
              PO BOX 9443 STN PROV GOVT
              VICTORIA BC V8W 9W7
              Courier Address
              Director
              Provincial Sales Tax
              Ministry of Finance
              1802 Douglas Street
              Victoria BC V8T 4K6
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>

      <v-tab-item>
        <v-card flat>
          <v-card-text>Cash only accepted through money-order in the amount of $XXX to Ministry of Agriculture</v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs>

    <!-- snippet-start: CTA To next page -->
    <v-layout>
      <v-flex ma-5>
        <v-btn large round block dark class="primary">
          <button @click="$router.push('review')">Review</button>
        </v-btn>
      </v-flex>
    </v-layout>
    <!-- end: -->
  </v-container>
</template>

import Navbar from "@/components/Navbar";


<script>
export default {
  data: () => ({
    mask: "",
    value: ""
  })
};
</script>