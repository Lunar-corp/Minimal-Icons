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
    <path d="m14 5-3 3 2 7 8-8-7-2Z" />
    <path d="m14 5-3 3-3-3 3-3 3 3Z" />
    <path d="M9.5 6.5 4 12l3 6" />
    <path d="M3 22v-2c0-1.1.9-2 2-2h4a2 2 0 0 1 2 2v2H3Z" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>