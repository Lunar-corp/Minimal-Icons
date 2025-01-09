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
    <path d="m21,5H3" /><path d="m5,11h-2" /><path d="m7,17H3" /><path d="m14,19h-1c-1.1,0-2-.9-2-2v-7" /><polyline points="9 11 11 9 13 11" /><path d="m16,9h1c1.1,0,2,.9,2,2v7" /><polyline points="21 17 19 19 17 17" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>