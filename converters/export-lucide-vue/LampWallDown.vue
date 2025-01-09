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
    <path d="M11 13h6l3 7H8l3-7Z" />
    <path d="M14 13V8a2 2 0 0 0-2-2H8" />
    <path d="M4 9h2a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H4v6Z" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>