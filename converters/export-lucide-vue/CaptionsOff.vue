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
    <path d="M10.5 5H19a2 2 0 0 1 2 2v8.5" />
    <path d="M17 11h-.5" />
    <path d="M19 19H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2" />
    <path d="m2 2 20 20" />
    <path d="M7 11h4" />
    <path d="M7 15h2.5" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>