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
    <path d="M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v2" />
    <path d="M14 2v4a2 2 0 0 0 2 2h4" />
    <circle cx="6" cy="14" r="3" />
    <path d="M6 10v1" />
    <path d="M6 17v1" />
    <path d="M10 14H9" />
    <path d="M3 14H2" />
    <path d="m9 11-.88.88" />
    <path d="M3.88 16.12 3 17" />
    <path d="m9 17-.88-.88" />
    <path d="M3.88 11.88 3 11" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>