<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m8,21h12c1.1,0,2-.9,2-2v-2h-12v2c0,1.1-.9,2-2,2s-2-.9-2-2V5c0-1.1-.9-2-2-2s-2,.9-2,2v3h4" /><path d="m20,17V5c0-1.1-.9-2-2-2H4" /><path d="m17,9.2c0-1.2-1-2.2-2.2-2.2-.8,0-1.4.3-1.8.9-.4-.6-1-.9-1.8-.9-1.2,0-2.2,1-2.2,2.2,0,.6.3,1.2.7,1.6h0c1.3,1.3,3.3,3.2,3.3,3.2,0,0,2-1.9,3.3-3.1h0c.4-.4.7-1,.7-1.7Z" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>